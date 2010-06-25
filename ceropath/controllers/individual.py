import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

from pprint import pprint
import os.path
import math
import os
from collections import defaultdict
import re

REGX_COI = re.compile('coi')
REGX_CYTB = re.compile('cytb')
REGX_PRIMER = re.compile('primer')
REGX_16S = re.compile('16s')

class IndividualController(BaseController):

    def show(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        path = os.path.join('data','morphologie des individus')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        upper_individual_id = individual['_id'].upper() 
        ## image
        image_path = ''
        for file_name in os.listdir(file_path):
            if upper_individual_id in file_name and 'side' in file_name.lower():
                image_path = os.path.join(server_path, file_name)
        ## sex
        if individual['sex'] == 'f':
            sex = 'female'
        elif individual['sex'] == 'm':
            sex = 'male'
        else:
            sex = 'unknown'
        measures_infos, publications_list = self._get_measurements(individual['_id'], individual['organism_classification']['_id'])
        return render('individual/infos.mako', extra_vars={
            '_id': individual['_id'],
            'species': individual['organism_classification']['_id'],
            'image_path':image_path,
            'sex': sex,
            'age': individual['adult'],
            'dissection_date': str(individual['dissection_date'].date()),
            'measures_infos': measures_infos,
            'publications_list': publications_list,
            'country': individual['trapping_informations']['site']['country'],
            'province': individual['trapping_informations']['site']['province'],
            'region': individual['trapping_informations']['site']['region'],
            'surrounding_landscape': individual['trapping_informations']['site']['surrounding_landscape'],
            'lat': individual['trapping_informations']['site']['coord_wgs']['dll_lat'].replace(',', '.'),
            'long': individual['trapping_informations']['site']['coord_wgs']['dll_long'].replace(',', '.'),
            'accuracy': individual['trapping_informations']['trap_accuracy'],
        })

    def _get_measurements(self, individual_id, species_id):
        species_measurements = list(self.db.species_measurement.SpeciesMeasurement.find(
          {'organism_classification.$id': species_id}
        ))
        measures_infos = {}
        publications_list = {}
        # species
        for measure in species_measurements:
            for pub in measure['pubref']:
                publications_list[pub['_id']] = pub
            for m in measure['measures']:
                trait, value = m['trait'], m['value']
                if trait not in measures_infos:
                    measures_infos[trait] = {}
                for publication in measure['pubref']:
                    if publication['_id'] not in measures_infos[trait]:
                        measures_infos[trait][publication['_id']] = {}
                    measures_infos[trait][publication['_id']][measure['type']] = value
        individual = self.db.individual.get_from_id(individual_id)
        # one individual
        for measure in individual['measures']:
            if measure['trait'] not in measures_infos:
                measures_infos[measure['trait']] = {}
            measures_infos[measure['trait']][individual_id] = measure['value']
        #publications_list[individual_id] = None
        # ceropath measurements for species
        species_measurements = {}
        individuals = self.db.individual.find({
            'organism_classification.$id': species_id,
            'adult':'adult',
            'identification.type':{'$in':[REGX_COI, REGX_CYTB, REGX_PRIMER, REGX_16S]}
        })
        nb_individuals = individuals.count()
        traits_list = []
        for individual in individuals:
            for measure in individual['measures']:
                trait  = measure['trait']
                if trait not in measures_infos:
                    measures_infos[trait][species_id] = {}
                if trait not in traits_list:
                    traits_list.append(trait)
                try:
                    value = float(measure['value'].replace(',', '.'))
                except:
                    continue
                if trait not in species_measurements:
                    species_measurements[trait] = {'value':0.0, 'max':0, 'min':999999999}
                species_measurements[trait]['value'] += value
                species_measurements[trait]['max'] = max(species_measurements[trait]['max'], value)
                species_measurements[trait]['min'] = min(species_measurements[trait]['min'], value)
        #publications_list[species_id] = None
        for individual in individuals.rewind():
            for measure in individual['measures']:
                trait = measure['trait']
                species_measurements[trait]['mean'] = species_measurements[trait]['value']/nb_individuals
                try:
                    value = float(measure['value'].replace(',', '.'))
                except:
                    continue
                variance = math.pow(value - species_measurements[trait]['mean'], 2)/(nb_individuals -1)
                species_measurements[trait]['sd'] = math.sqrt(math.pow(variance,2)/nb_individuals)
        for trait in traits_list:
            if species_id not in measures_infos[trait]:
                measures_infos[trait][species_id] = {}
            measures_infos[trait][species_id]['mean'] = round(species_measurements[trait]['mean'], 2)
            measures_infos[trait][species_id]['max'] = species_measurements[trait]['max']
            measures_infos[trait][species_id]['min'] = species_measurements[trait]['min']
            measures_infos[trait][species_id]['min'] = species_measurements[trait]['min']
            measures_infos[trait][species_id]['sd'] = round(species_measurements[trait]['sd'], 2)
            measures_infos[trait][species_id]['n'] = nb_individuals
        return measures_infos, publications_list
 

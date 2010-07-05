import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from config import google_map_api_key

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
                    measures_infos[trait] = {}
                if species_id not in measures_infos[trait]:
                    measures_infos[trait][species_id] = {}
                if trait not in traits_list:
                    traits_list.append(trait)
                if trait not in species_measurements:
                    species_measurements[trait] = {'value':0.0, 'max':0, 'min':999999999}
                try:
                    value = float(measure['value'].replace(',', '.'))
                except:
                    continue
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
            if 'sd' in species_measurements[trait]:
                measures_infos[trait][species_id]['sd'] = round(species_measurements[trait]['sd'], 2)
                measures_infos[trait][species_id]['n'] = nb_individuals
            else:
                measures_infos[trait][species_id]['sd'] = None
                measures_infos[trait][species_id]['n'] = None
        return measures_infos, publications_list
 
    def show(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        path = os.path.join('data','static', 'vouchers skull pictures with measurements')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        upper_individual_id = individual['_id'].upper() 
        ## image
        image_path = ''
        for file_name in os.listdir(file_path):
            if id in file_name.lower():
                image_path = os.path.join(server_path, file_name)
        ## sex
        if individual['sex'] == 'f':
            sex = 'female'
        elif individual['sex'] == 'm':
            sex = 'male'
        else:
            sex = 'unknown'
        measures_infos, publications_list = self._get_measurements(individual['_id'], individual['organism_classification']['_id'])
        sequences = dict((i['gene']['$id'], i) for i in self.db.sequence.find({'individual.$id':id}))
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
            'latitude': individual['trapping_informations']['site']['coord_wgs']['dll_lat'],
            'longitude': individual['trapping_informations']['site']['coord_wgs']['dll_long'],
            'accuracy': individual['trapping_informations']['trap_accuracy'],
            'voucher': individual['voucher_barcoding'],
            'sequences': sequences,
            'api_key': google_map_api_key,
        })

    def sequence(self, id, gene):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        sequence = self.db.sequence.find_one({'gene.$id':gene.lower(), 'individual.$id':id})
        if not sequence:
            abort(404)
        if not sequence['internet_display']:
            abort(401)
        fasta_name = "%s-%s" % ( id, "_".join(individual['organism_classification']['_id'].split()))
        response.headers['Content-type'] = 'text/x-fasta'
        response.headers['Content-disposition'] = 'attachment; filename=%s.fasta' % fasta_name
        return ">%s\n%s\n" % (fasta_name.encode('utf-8'), sequence['sequence'].encode('utf-8'))

    def trapping(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        house_number = individual['trapping_informations']['site']['house']['number']
        if house_number is not None:
            house_number = math.pow(10, house_number)
        house_distance = individual['trapping_informations']['site']['house']['distance']
        if house_distance is not None:
            house_distance = math.pow(10, house_distance)
        path = os.path.join('data','static', 'trap lines pictures')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        upper_site_id = individual['trapping_informations']['site']['_id'].upper() 
        image_paths = []
        for file_name in os.listdir(file_path):
            if upper_site_id in file_name:
                image_paths.append(os.path.join(server_path, file_name))
        return render('individual/trapping.mako', extra_vars={
            '_id': individual['_id'],
            'species': individual['organism_classification']['_id'],
            'region': individual['trapping_informations']['site']['region'],
            'country': individual['trapping_informations']['site']['country'],
            'province': individual['trapping_informations']['site']['province'],
            'district': individual['trapping_informations']['site']['district'],
            'sub_district': individual['trapping_informations']['site']['sub_district'],
            'village': individual['trapping_informations']['site']['village'],
            'surrounding_landscape': individual['trapping_informations']['site']['surrounding_landscape'],
            'latitude': individual['trapping_informations']['site']['coord_wgs']['dll_lat'],
            'longitude': individual['trapping_informations']['site']['coord_wgs']['dll_long'],
            'house_presence': individual['trapping_informations']['site']['house']['presence'],
            'house_number': 'unknown' if house_number is None else int(house_number),
            'house_distance': 'unknown' if house_distance is None else int(house_distance),
            'accuracy': individual['trapping_informations']['trap_accuracy'],
            'site': individual['trapping_informations']['site']['_id'],
            'image_paths': image_paths,
            'api_key': google_map_api_key,
        })

    def module(self, id, name):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        return render('individual/module.mako', extra_vars={
            '_id': id,
            'species': individual['organism_classification']['_id'],
            'name': name,
        })

    def parasites(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(401)
        rel_host_parasites_list = self.db.rel_host_parasite.find({'host.$id':individual['organism_classification']['_id']})
        rel_host_parasites = {}
        for rhp in rel_host_parasites_list:
            rel_host_parasites[rhp['_id']] = (rhp, self.db.publication.get_from_id(rhp['pubref']['$id']))
        return render('individual/parasites.mako', extra_vars={
            'rel_host_parasites':rel_host_parasites,
            '_id': id,
        })
 

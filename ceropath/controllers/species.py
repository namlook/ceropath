import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
import os.path
import os

log = logging.getLogger(__name__)

from pprint import pprint

import re
import math
REGX_COI = re.compile('coi')
REGX_CYTB = re.compile('cytb')
REGX_PRIMER = re.compile('primer')
REGX_16S = re.compile('16s')

class SpeciesController(BaseController):

    def _get_measurements(self, species_id):
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
 

    def index(self):
        species_list = self.db.organism_classification.OrganismClassification.find(
          {'internet_display': True, 'type': 'mammal'}
        ).sort('_id', 1)
        return render('species/index.mako', extra_vars={
            'species_list':species_list
        })

    def show(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        if not species['internet_display']:
            abort(404)
        path = os.path.join('data','photos des animaux vivants')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        capitalized_species_id = species['_id'].capitalize() 
        ## description
        description = ""
        if '%s.txt' % capitalized_species_id in os.listdir(file_path):
            description = open(os.path.join(file_path, '%s.txt' % capitalized_species_id)).read()
        ## image
        image_path = ''
        if '%s_1.jpg' % capitalized_species_id in os.listdir(file_path):
            image_path = os.path.join(server_path, '%s_1.jpg' % capitalized_species_id)
        return render('species/infos.mako', extra_vars={
            '_id': species['_id'],
            'iucn_id': species['iucn']['id'],
            'taxonomic_rank': species['taxonomic_rank'],
            'common_names': species['name']['common'],
            'description': description,
            'image_path': image_path,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'synonyms': dict((i['name'], i['pubref']) for i in species['synonyms'] if i['name'] != species['_id']),
        })

    def measurements(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        if not species['internet_display']:
            abort(401)
#        species_measurements = list(self.db.species_measurement.SpeciesMeasurement.find(
#          {'organism_classification.$id': id}
#        ))
#        measures_infos = {}
#        publications_list = {}
#        for measure in species_measurements:
#            for pub in measure['pubref']:
#                publications_list[pub['_id']] = pub
#            for m in measure['measures']:
#                trait, value = m['trait'], m['value']
#                if trait not in measures_infos:
#                    measures_infos[trait] = {}
#                for publication in measure['pubref']:
#                    if publication['_id'] not in measures_infos[trait]:
#                        measures_infos[trait][publication['_id']] = {}
#                    measures_infos[trait][publication['_id']][measure['type']] = value
        measures_infos, publications_list = self._get_measurements(id)
        return render('species/measurements.mako', extra_vars={
            '_id': species['_id'],
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'measures_infos': measures_infos,
            'publications_list': publications_list,
        })
        
    def module(self, id, name):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        if not species['internet_display']:
            abort(401)
#        module_path = os.path.join('ceropath', 'public', 'data')
#        if name not in os.listdir(module_path):
#            abort(404)
#        # TODO good
#        #if id not in os.listdir(os.path.join(module_path, name)):
#        #    abort(404)
#        # XXX a supprimer
#        files_list = []
#        legends = {}
#        for file_name in os.listdir(os.path.join(module_path, name)):
#            if id in file_name.lower():
#                base_file_name, ext = os.path.splitext(file_name)
#                if ext == '.txt':
#                    legend_file = os.path.join(module_path, '%s.txt' % base_file_name)
#                    if '%s.txt' % base_file_name in os.listdir(module_path):
#                        legends[file_name] = open(legend_file).read()
#                if ext == '.jpg':
#                    files_list.append(file_name)
        return render('species/module.mako', extra_vars={
            '_id': species['_id'],
            'name': name,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
#            'files_list': files_list,
#            'legends': legends,
#            'data_path': os.path.join('/', 'data', name),
        })
        
    def individuals(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        individuals_list = self.db.individual.find(
          {'internet_display': True, 'organism_classification.$id':id}
        ).sort('_id', 1)
        individuals = {}
        for individual in individuals_list:
            site_id = individual['trapping_informations']['site']
            if site_id:
                site_id = site_id.id
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site)
        return render('individual/list.mako', extra_vars={
            'individuals':individuals,
            'species': id,
        })

    def vouchers(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        individuals_list = self.db.individual.find(
          {'internet_display': True, 'organism_classification.$id':id, 'voucher_barcoding':True}
        ).sort('_id', 1)
        individuals = {}
        for individual in individuals_list:
            site_id = individual['trapping_informations']['site']
            if site_id:
                site_id = site_id.id
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site)
        return render('individual/list.mako', extra_vars={
            'species': id,
            'individuals':individuals,
        })

    def sampling_map(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        individuals_list = self.db.individual.find(
          {'internet_display': True, 'organism_classification.$id':id}
        ).sort('_id', 1)
        individuals = {}
        for individual in individuals_list:
            site_id = individual['trapping_informations']['site']
            if site_id:
                site_id = site_id.id
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site )
        return render('species/sampling_map.mako', extra_vars={
            '_id': species['_id'],
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'individuals': individuals,
        })
 
    def parasites(self, id):
        rel_host_parasites = self.db.rel_host_parasite.RelHostParasite.find({'host.$id':id})
        return render('species/parasites.mako', extra_vars={
            'rel_host_parasites':rel_host_parasites,
            'species': id,
        })


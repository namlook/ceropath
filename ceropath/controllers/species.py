import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
import os.path
import os

log = logging.getLogger(__name__)

from pprint import pprint

class SpeciesController(BaseController):

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
            abort(401)
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
            'synonyms': set(i['name'] for i in species['synonyms'] if i['name'] != species['_id'])
        })


    def measurements(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        if not species['internet_display']:
            abort(401)
        species_measurements = list(self.db.species_measurement.SpeciesMeasurement.find(
          {'organism_classification.$id': id}
        ))
        measures_infos = {}
        publications_list = {}
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
        module_path = os.path.join('ceropath', 'public', 'data')
        print os.listdir(module_path)
        if name not in os.listdir(module_path):
            abort(404)
        # TODO good
        #if id not in os.listdir(os.path.join(module_path, name)):
        #    abort(404)
        # XXX a supprimer
        files_list = []
        legends = {}
        for file_name in os.listdir(os.path.join(module_path, name)):
            if id in file_name.lower():
                base_file_name, ext = os.path.splitext(file_name)
                if ext == '.txt':
                    legend_file = os.path.join(module_path, '%s.txt' % base_file_name)
                    if '%s.txt' % base_file_name in os.listdir(module_path):
                        legends[file_name] = open(legend_file).read()
                if ext == '.jpg':
                    files_list.append(file_name)
        return render('species/module.mako', extra_vars={
            '_id': species['_id'],
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'files_list': files_list,
            'legends': legends,
            'data_path': os.path.join('/', 'data', name),
        })
        
    def individuals(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        individuals_list = self.db.individual.find(
          {'internet_display': True, 'organism_classification.$id':id}
        ).sort('_id', 1)
        return render('individual/list.mako', extra_vars={
            'individuals_list':individuals_list
        })
 

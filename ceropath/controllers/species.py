import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons.decorators.cache import beaker_cache

from config import google_map_api_key

from ceropath.lib.base import BaseController, render
import os.path
import os
import urllib2

log = logging.getLogger(__name__)

from pprint import pprint
import anyjson

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
        query = {
            'organism_classification.$id': species_id,
            'adult':'adult',
            'identification.type':{'$in':[REGX_COI, REGX_CYTB, REGX_PRIMER, REGX_16S]}
        }
        individuals = self.db.individual.find(query)
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
        REGEXP_NUMBER = re.compile('^[\d\.,]+$')
        nb_individuals = {}
        for individual in individuals.rewind():
            for measure in individual['measures']:
                trait = measure['trait']
                query['measures'] = {'$elemMatch':{'trait': trait, 'value': REGEXP_NUMBER}}
                if not trait in nb_individuals.get(individual['_id'], []): 
                    if individual['_id'] not in nb_individuals:
                        nb_individuals[individual['_id']] = {}
                    nb_individuals[individual['_id']][trait] = self.db.individual.find(query).count()
                nb_individual = nb_individuals[individual['_id']][trait]
                if nb_individual:
                    species_measurements[trait]['mean'] = species_measurements[trait]['value']/nb_individual
                    try:
                        value = float(measure['value'].replace(',', '.'))
                    except:
                        continue
                    variance = math.pow(value - species_measurements[trait]['mean'], 2)/(nb_individual -1)
                    species_measurements[trait]['sd'] = math.sqrt(math.pow(variance,2)/nb_individual)
        for trait in traits_list:
            if species_id not in measures_infos[trait]:
                measures_infos[trait][species_id] = {}
            if 'sd' in species_measurements[trait]:
                measures_infos[trait][species_id]['mean'] = round(species_measurements[trait]['mean'], 2)
                measures_infos[trait][species_id]['max'] = species_measurements[trait]['max']
                measures_infos[trait][species_id]['min'] = species_measurements[trait]['min']
                measures_infos[trait][species_id]['sd'] = round(species_measurements[trait]['sd'], 2)
                measures_infos[trait][species_id]['n'] = nb_individuals[individual['_id']][trait]
            else:
                measures_infos[trait][species_id]['mean'] = None
                measures_infos[trait][species_id]['max'] = None
                measures_infos[trait][species_id]['min'] = None
                measures_infos[trait][species_id]['sd'] = None
                measures_infos[trait][species_id]['n'] = None
        return measures_infos, publications_list
 

    def index(self):
        query = {'internet_display': True, 'type': 'mammal'}
        filter = request.params.get('as_values_filter')
        enable_back = False
        if filter:
            enable_back = True
            pattern, field = filter.strip(',').split('|')
            search_pattern = re.compile(pattern)
            query['taxonomic_rank.%s' % field] = search_pattern
        species_list = self.db.organism_classification.OrganismClassification.find(
            query
        ).sort('_id', 1)
        return render('species/index.mako', extra_vars={
            'species_list':species_list,
            'enable_back': enable_back,
        })

    def show(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        path = os.path.join('data','static', 'alive animals')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        capitalized_species_id = species['_id'].capitalize() 
        ## description
        description = ""
        if '%s.txt' % capitalized_species_id in os.listdir(file_path):
            description = open(os.path.join(file_path, '%s.txt' % capitalized_species_id)).read()
        ## image
        image_paths = []
        for file_name in os.listdir(file_path):
            image_path = ''
            photo_author = ''
            base, ext = os.path.splitext(file_name)
            if species['_id'] in file_name.lower() and ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                image_path = os.path.join(server_path, file_name)
                if len(file_name.split('(')) > 1:
                    photo_author = file_name.split('(')[1].split(')')[0]
                image_paths.append((image_path, photo_author))
        citations = species['citations']
        genus_citations = self.db.organism_classification.OrganismClassification.find_one(
            { '_id':'%s sp.' % species['taxonomic_rank']['genus'] }
        )
        _d_citations = dict((i['pubref']['_id'], i['name']) for i in citations)
        if genus_citations:
            for cit in genus_citations['citations']:
                if 'sp.' in cit['name']:
                    genus = cit['name'].split()[0]
                    if genus in _d_citations.get(cit['pubref']['_id'], ''):
                        genus_citations['citations'].remove(cit)
            citations.extend(genus_citations['citations'])
        iucn_map_path = os.path.join('ceropath', 'public', 'iucn')
        iucn_web_path = os.path.join('/', 'iucn')
        iucn_id = species['iucn']['id']
        if not '%s.png' % iucn_id in os.listdir(iucn_map_path):
            try:
                open(os.path.join(iucn_map_path, '%s.png' % iucn_id), 'w').write(
                  urllib2.urlopen('http://www.iucnredlist.org/apps/redlist/images/range/maps/%s.png' % iucn_id).read()
                )
            except:
                print "cannot fetch %s" % iucn_id
                iucn_web_path = None
        return render('species/infos.mako', extra_vars={
            '_id': species['_id'],
            'iucn_id': species['iucn']['id'],
            'id_msw3': species['id_msw3'],
            'taxonomic_rank': species['taxonomic_rank'],
            'common_names': species['name']['common'],
            'description': description,
            'image_paths': image_paths,
            'photo_author': photo_author,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'synonyms': species['synonyms'],
            'citations': citations,
            'internet_display': species['internet_display'],
            'iucn_web_path': iucn_web_path, 
        })

    @beaker_cache(type='memory', query_args=True)
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
                site_id = site_id['$id']
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site)
        return render('species/individuals.mako', extra_vars={
            '_id': id,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'individuals':individuals,
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
                site_id = site_id['$id']
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site)
        return render('species/vouchers.mako', extra_vars={
            '_id': id,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'individuals':individuals,
        })

    def sampling_map(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        individuals_list = self.db.individual.find(
          {'internet_display': True, 'organism_classification.$id':id}
        )
        individuals = {}
        for individual in individuals_list:
            site_id = individual['trapping_informations']['site']
            if site_id:
                site_id = site_id['$id']
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site )
        return render('species/sampling_map.mako', extra_vars={
            '_id': species['_id'],
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'individuals': individuals,
            'api_key': google_map_api_key,
        })
 
    def parasites(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        rel_host_parasites_list = self.db.rel_host_parasite.find({'host.$id': id})
        rel_host_parasites = {}
        for rhp in rel_host_parasites_list:
            rel_host_parasites[rhp['_id']] = (rhp, self.db.publication.get_from_id(rhp['pubref']['$id']))
        return render('species/parasites.mako', extra_vars={
            '_id': id,
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'rel_host_parasites':rel_host_parasites,
        })

    def filter(self):
        q = request.params.get('q')
        search_pattern = re.compile(q.lower())
        results = []
        for rank in ['family', 'genus', 'tribe', 'class', 'order']:
            dbres = self.db.organism_classification.find(
              {'taxonomic_rank.%s' % rank:search_pattern},
              fields=['taxonomic_rank.%s'%rank]
            )
            for res in dbres:
                line = {
                  'name':"%s (%s)" % (res['taxonomic_rank'][rank], rank),
                  'value': "%s|%s" % (res['taxonomic_rank'][rank], rank),
                }
                if line not in results:
                    results.append(line)
        response.headers['Content-type'] = 'application/json'
        return anyjson.serialize(results)

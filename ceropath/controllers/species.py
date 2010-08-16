import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons.decorators.cache import beaker_cache

from config import google_map_api_key

from ceropath.lib.base import BaseController, render
from ceropath.lib import helpers as h
import os.path
import os
import urllib2

log = logging.getLogger(__name__)

from pprint import pprint
import anyjson
import codecs

import re


class SpeciesController(BaseController):
    """
    This controller handle actions for objects from the
    collection`organism_classification`.  While an OrganismClassification can
    be either a mammal or a parasite, this controller only look at the mammal
    ones. Please take a look to the `ParasiteController` for parasites actions.

    In general Controller's actions only treat objects which have their
    `internetr_display` as True.
    """

    # actions which require a login are listed below
    requires_auth_actions = ['individuals']

    def index(self):
        """
        Show the list of mammal proceed by the CERoPath project.
        """
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
            'title': 'species',
        })

    def show(self, id):
        """
        Show informations about the mammal.
        """
        id = id.lower()
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species or species['type'] != 'mammal':
            abort(404)
        path = os.path.join('data','static', 'alive animals')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        capitalized_species_id = species['_id'].capitalize() 
        ## description
        description = ""
        if '%s.txt' % capitalized_species_id in os.listdir(file_path):
            description = codecs.open(os.path.join(file_path, '%s.txt' % capitalized_species_id), 'r', 'utf-8', errors='ignore').read()
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
        # citations
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
        citations = sorted([(h.author_date_from_citation(cit['pubref']['reference']), cit) for cit in citations])
        # iucn map
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
            'author_date': species['reference']['biblio']['author_date'],
            'synonyms': species['synonyms'],
            'citations': citations,
            'internet_display': species['internet_display'],
            'iucn_web_path': iucn_web_path, 
            'has_individuals': self.db.individual.find({'organism_classification.$id':species['_id']}).count(),
            'title': '%s informations' % id.capitalize(),
        })

    def measurements(self, id):
        """
        Show the mammal measurements tab
        """
        id = id.lower()
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species or species['type'] != 'mammal':
            abort(404)
        if not species['internet_display']:
            abort(404)
        measures_infos = {}
        publications_list = []
        for measure in species['measures_stats']:
            pubref = measure['pubref']
            origin = measure['origin']
            species_article_name = measure['species_article_name']
            publications_list.append((pubref, origin, species_article_name))
            for trait in measure['measures']:
                if trait not in measures_infos:
                    measures_infos[trait] = {}
                if (pubref, origin, species_article_name) not in measures_infos[trait]:
                    measures_infos[trait][(pubref, origin, species_article_name)] = {}
                measures_infos[trait][(pubref, origin, species_article_name)] = measure['measures'][trait]
        traits = dict((int(i['_id']), i) for i in self.db.trait.find())
        ## image
        path = os.path.join('data','static', 'measurements')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        image_paths = []
        for file_name in os.listdir(file_path):
            image_paths.append(os.path.join(server_path, file_name))
        return render('species/measurements.mako', extra_vars={
            '_id': species['_id'],
            'author_date': species['reference']['biblio']['author_date'],
            'measures_infos': measures_infos,
            'publications_list': publications_list,
            'traits': traits,
            'image_paths': image_paths,
            'title': "%s's measurements" % id.capitalize(),
        })
        
    def module(self, id, name):
        """
        This action take a mammal id an a module name. A Module is a way to
        display photos and texts which are present into the
        `public/data/dynamic` directory
        """
        id = id.lower()
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        if not species['internet_display']:
            abort(404)
        return render('species/module.mako', extra_vars={
            '_id': species['_id'],
            'name': name,
            'author_date': species['reference']['biblio']['author_date'],
            'title': "%s's %s" % (id.capitalize(), name),
        })
        
    def individuals(self, id):
        """
        Show all mamal's individual which have their `internet_display` field
        to True. Not that user must be authorized to display perform this action.
        """
        id = id.lower()
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
        return render('species/individuals.mako', extra_vars={
            '_id': id,
            'author_date': species['reference']['biblio']['author_date'],
            'individuals':individuals,
            'title': "%s's individuals" % id.capitalize(),
        })

    def vouchers(self, id):
        """
        Show all the mammal's vouchers.
        """
        id = id.lower()
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
        return render('species/vouchers.mako', extra_vars={
            '_id': id,
            'author_date': species['reference']['biblio']['author_date'],
            'individuals':individuals,
            'title': "%s's vouchers" % id.capitalize(),
        })

    def sampling_map(self, id):
        """
        Show the sampling map of all mammal's individual which have their
        `internet_display` field set to True.
        """
        id = id.lower()
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
                site_id = site_id.id
            site = self.db.site.get_from_id(site_id)
            individuals[individual['_id']] = (individual, site )
        return render('species/sampling_map.mako', extra_vars={
            '_id': species['_id'],
            'author_date': species['reference']['biblio']['author_date'],
            'individuals': individuals,
            'api_key': google_map_api_key,
            'title': "%s's sampling map" % id.capitalize(),
        })
 
    def parasites(self, id):
        """
        Show all the mammal's parasites
        """
        id = id.lower()
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not species:
            abort(404)
        rel_host_parasites_list = self.db.rel_host_parasite.find({'host.$id':id}).sort('parasite.$id')#taxonomic_rank.class', 1)
        rel_host_parasites = {}
        for rhp in rel_host_parasites_list:
            parasite_id = rhp['parasite']
            if parasite_id:
                parasite_id = parasite_id.id
            parasite = self.db.organism_classification.get_from_id(parasite_id)
            if parasite is None:
                continue
            kingdom = parasite['taxonomic_rank']['kingdom']
            _class = parasite['taxonomic_rank']['class']
            if kingdom not in rel_host_parasites:
                rel_host_parasites[kingdom] = {}
            if not _class in rel_host_parasites[kingdom]:
                rel_host_parasites[kingdom][_class] = []
            try:
                rel_host_parasites[kingdom][_class].append((rhp, parasite, self.db.publication.get_from_id(rhp['pubref']['$id'])))
            except:
                rel_host_parasites[kingdom][_class].append((rhp, parasite, self.db.publication.get_from_id(rhp['pubref'].id)))
        return render('species/parasites.mako', extra_vars={
            '_id': id,
            'author_date': species['reference']['biblio']['author_date'],
            'rel_host_parasites':rel_host_parasites,
            'title': "%s's parasites" % id.capitalize(),
        })

    def filter(self):
        """
        autocompletion action. Used by the action `index`
        """
        q = request.params.get('q')
        search_pattern = re.compile(q.lower())
        results = []
        for rank in ['family', 'genus', 'tribe', 'class', 'order']:
            dbres = self.db.organism_classification.find(
              {'type':'mammal', 'taxonomic_rank.%s' % rank:search_pattern},
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

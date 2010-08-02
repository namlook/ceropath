import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

import os
import re
import anyjson

REGX_COI = re.compile('coi')
REGX_CYTB = re.compile('cytb')
REGX_PRIMER = re.compile('primer')
REGX_16S = re.compile('16s')

log = logging.getLogger(__name__)

class ParasiteController(BaseController):

    def index(self):
        query = {'internet_display': True, 'type': 'parasite'}
        filter = request.params.get('as_values_filter')
        enable_back = False
        if filter:
            enable_back = True
            pattern, field = filter.strip(',').split('|')
            search_pattern = re.compile(pattern)
            query['taxonomic_rank.%s' % field] = search_pattern
        parasites_list = self.db.organism_classification.find(
            query
        ).sort('taxonomic_rank.class', 1)
        parasites = {}
        for parasite in parasites_list:
            kingdom = parasite['taxonomic_rank']['kingdom']
            if kingdom not in parasites:
                parasites[kingdom] = []
            parasites[kingdom].append(parasite)
        return render('parasite/index.mako', extra_vars={
            'parasites': parasites,
            'enable_back': enable_back,
            'title': 'parasites',
        })


    def show(self, id):
        species = request.params.get('species')
        individual = request.params.get('individual')
        parasite = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not parasite:
            abort(404)
        if not parasite['internet_display']:
            abort(401)
        #path = os.path.join('data','static', 'parasites')
        #file_path =  os.path.join('ceropath', 'public', path)
        #server_path = os.path.join('/', path)
        #capitalized_parasite_id = parasite['_id'].capitalize() 
        ## image
        #image_path = ''
        #for file_name in os.listdir(file_path):
        #    base, ext = os.path.splitext(file_name)
        #    if parasite['_id'] in file_name.lower() and ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        #        image_path = os.path.join(server_path, file_name)
        rel_host_parasites = self.db.rel_host_parasite.RelHostParasite.find({'parasite.$id':id})
        rel_host_parasites = dict(((i['host']['_id'], i['pubref']['_id']), i) for i in rel_host_parasites)
        citations = parasite['citations']
        genus_citations = self.db.organism_classification.OrganismClassification.find_one(
            { '_id':'%s sp.' % parasite['taxonomic_rank']['genus'] }
        )
        _d_citations = dict((i['pubref']['_id'], i['name']) for i in citations)
        if genus_citations:
            for cit in genus_citations['citations']:
                if 'sp.' in cit['name']:
                    genus = cit['name'].split()[0]
                    if genus in _d_citations.get(cit['pubref']['_id'], ''):
                        genus_citations['citations'].remove(cit)
            citations.extend(genus_citations['citations'])
        return render('parasite/show.mako', extra_vars={
            '_id': parasite['_id'],
            'taxonomic_rank': parasite['taxonomic_rank'],
            'common_names': parasite['name']['common'],
            'author': parasite['reference']['biblio']['author'],
            'date': parasite['reference']['biblio']['date'],
            'synonyms': parasite['synonyms'],
            'citations': citations,
            'species': species,
            'individual': individual,
            'author_date': parasite['reference']['biblio']['author_date'],
            'rel_host_parasites': rel_host_parasites,
            'title': '%s' % id.capitalize(),
        })

    def filter(self):
        q = request.params.get('q')
        search_pattern = re.compile(q.lower())
        results = []
        for rank in ['family', 'genus', 'tribe', 'class', 'order']:
            dbres = self.db.organism_classification.find(
              {'type':'parasite', 'taxonomic_rank.%s' % rank:search_pattern},
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

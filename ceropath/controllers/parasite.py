import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

import os

log = logging.getLogger(__name__)

class ParasiteController(BaseController):

    def show(self, id):
        species = request.params.get('species')
        individual = request.params.get('individual')
        parasite = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not parasite:
            abort(404)
        if not parasite['internet_display']:
            abort(401)
        path = os.path.join('data','static', 'parasites')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        capitalized_parasite_id = parasite['_id'].capitalize() 
        ## image
        image_path = ''
        for file_name in os.listdir(file_path):
            base, ext = os.path.splitext(file_name)
            if parasite['_id'] in file_name.lower() and ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                image_path = os.path.join(server_path, file_name)
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
            'image_path': image_path,
            'author': parasite['reference']['biblio']['author'],
            'date': parasite['reference']['biblio']['date'],
            'synonyms': parasite['synonyms'],#set(i['name'] for i in parasite['synonyms'] if i['name'] != parasite['_id']),
            'citations': citations,
            'species': species,
            'individual': individual,
            'rel_host_parasites': rel_host_parasites
        })


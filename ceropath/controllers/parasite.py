import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

import os

log = logging.getLogger(__name__)

class ParasiteController(BaseController):

    def show(self, id):
        species = request.params.get('species')
        parasite = self.db.organism_classification.OrganismClassification.get_from_id(id)
        if not parasite:
            abort(404)
        if not parasite['internet_display']:
            abort(401)
        path = os.path.join('data','photos des animaux vivants')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        capitalized_parasite_id = parasite['_id'].capitalize() 
        ## image
        image_path = ''
        if '%s_1.jpg' % capitalized_parasite_id in os.listdir(file_path):
            image_path = os.path.join(server_path, '%s_1.jpg' % capitalized_parasite_id)
        return render('parasite/show.mako', extra_vars={
            '_id': parasite['_id'],
            'taxonomic_rank': parasite['taxonomic_rank'],
            'common_names': parasite['name']['common'],
            'image_path': image_path,
            'author': parasite['reference']['biblio']['author'],
            'date': parasite['reference']['biblio']['date'],
            'synonyms': set(i['name'] for i in parasite['synonyms'] if i['name'] != parasite['_id']),
            'species': species,
        })


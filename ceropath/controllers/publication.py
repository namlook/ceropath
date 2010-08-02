import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

import os

class PublicationController(BaseController):

    def show(self, id):
        publication = self.db.publication.get_from_id(id)
        if not publication:
            abort(404)
        # host related
        hosts_related = {}
        for species in self.db.organism_classification.find({'citations.pubref.$id':id, 'internet_display':True, 'type':'mammal'}):
            for citation in species['citations']:
                is_ok = False
                try:
                    is_ok = citation['pubref']['$id'] == id # XXX why $id ?
                except:
                    is_ok = citation['pubref'].id == id
                if is_ok:
                    if species['_id'] not in hosts_related:
                        hosts_related[species['_id']] = []
                    if citation['name'] != species['_id']:
                        hosts_related[species['_id']].append(citation['name'])
        # parasite related
        parasites_related = {}
        for species in self.db.organism_classification.find({'citations.pubref.$id':id, 'internet_display':True, 'type':'parasite'}):
            for citation in species['citations']:
                is_ok = False
                try:
                    is_ok = citation['pubref']['$id'] == id # XXX why $id ?
                except:
                    is_ok = citation['pubref'].id == id
                if is_ok:
                    if species['_id'] not in parasites_related:
                        parasites_related[species['_id']] = []
                    if citation['name'] != species['_id']:
                        parasites_related[species['_id']].append(citation['name'])
        pdfpath = ""
        if "%s.pdf" % publication['_id'] in os.listdir(os.path.join('ceropath', 'public', 'data', 'static', 'pdf')):
            pdfpath = os.path.join('/', 'data', 'static', 'pdf', "%s.pdf" % publication['_id'])
        return render('publication/show.mako', extra_vars={
            'reference': publication['reference'],
            'hosts_related': hosts_related,
            'parasites_related': parasites_related,
            'link': publication['link'],
            'pdfpath': pdfpath,
            'title': publication['reference'],
        })

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PublicationController(BaseController):

    def show(self, id):
        publication = self.db.publication.get_from_id(id)
        rel_host_parasites = self.db.rel_host_parasite.find({'pubref.$id':id})
        hosts_related = set([])
        parasites_related = set([])
        synonyms_related = {}
        for species in self.db.organism_classification.find({'synonyms.pubref.$id':id}):
            for synonym in species['synonyms']:
                if synonym['pubref'].id == id:
                    if synonym['name'] != species['_id']:
                        if species['_id'] not in synonyms_related:
                            synonyms_related[species['_id']] = []
                        synonyms_related[species['_id']].append(synonym['name'])
        for rhp in rel_host_parasites:
            hosts_related.add(rhp['host'].id)
            parasites_related.add(rhp['parasite'].id)
        return render('publication/show.mako', extra_vars={
            '_id': publication['_id'],
            'source': publication['source'],
            'reference': publication['reference'],
            'parasites_related': sorted(parasites_related),
            'hosts_related': sorted(hosts_related),
            'synonyms_related': synonyms_related,
        })

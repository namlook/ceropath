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
        # parasite synonyms related
        parasite_synonyms_related = {}
        for parasite in self.db.organism_classification.find({'synonyms.pubref.$id':id, 'internet_display':True, 'type':'parasite'}):
            for synonym in parasite['synonyms']:
                if synonym['pubref']['$id'] == id: # XXX why $id ?
                    if synonym['name'] != parasite['_id']:
                        if parasite['_id'] not in parasite_synonyms_related:
                            parasite_synonyms_related[parasite['_id']] = []
                        parasite_synonyms_related[parasite['_id']].append(synonym['name'])
        # host synonyms related
        host_synonyms_related = {}
        for species in self.db.organism_classification.find({'synonyms.pubref.$id':id, 'internet_display':True, 'type':'mammal'}):
            for synonym in species['synonyms']:
                is_ok = False
                if synonym['pubref'].id == id:
                    if synonym['name'] != species['_id']:
                        if species['_id'] not in host_synonyms_related:
                            host_synonyms_related[species['_id']] = []
                        host_synonyms_related[species['_id']].append(synonym['name'])
        for rhp in rel_host_parasites:
            hosts_related.add(rhp['host']['$id'])
            parasites_related.add(rhp['parasite']['$id'])
        return render('publication/show.mako', extra_vars={
            '_id': publication['_id'],
            'source': publication['source'],
            'reference': publication['reference'],
            'parasites_related': sorted(parasites_related),
            'hosts_related': sorted(hosts_related),
            'host_synonyms_related': host_synonyms_related,
            'parasite_synonyms_related': parasite_synonyms_related,
        })

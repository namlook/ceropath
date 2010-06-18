import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

from pprint import pprint

class SpeciesController(BaseController):

    def index(self):
        species_list = self.db.organism_classification.OrganismClassification.find(
          {'internet_display': True, 'type': 'mammal'}
        )
        return render('species/index.mako', extra_vars={
            'species_list':species_list
        })

    def show(self, id):
        species = self.db.organism_classification.OrganismClassification.get_from_id(id)
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
        return render('species/show.mako', extra_vars={
            '_id': species['_id'],
            'author': species['reference']['biblio']['author'],
            'date': species['reference']['biblio']['date'],
            'measures_infos': measures_infos,
            'publications_list': publications_list,
            'taxonomic_rank': species['taxonomic_rank'],
            'common_names': species['name']['common'],
        })

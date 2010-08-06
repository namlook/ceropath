import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from config import google_map_api_key

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

from pprint import pprint
import os.path
import math
import os
import re

REGEXP_NUMBER = re.compile('^[\d\.,]+$')

class IndividualController(BaseController):
 
    def show(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        if not individual['voucher_barcoding'] and 'user' not in session:
            abort(401)
        path = os.path.join('data','static', 'vouchers skull pictures with measurements')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        upper_individual_id = individual['_id'].upper() 
        ## image
        image_path = ''
        for file_name in os.listdir(file_path):
            if id in file_name.lower():
                image_path = os.path.join(server_path, file_name)
        ## sex
        if individual['sex'] == 'f':
            sex = 'female'
        elif individual['sex'] == 'm':
            sex = 'male'
        else:
            sex = 'unknown'
        species = individual['organism_classification']
        if not species:
            abort(404)
        measures_infos, publications_list, traits = self._measurements(individual, species)
        sequences = dict((i['gene'].id, i) for i in self.db.sequence.find({'individual.$id':id}))
        dissection_date = ''
        if individual['dissection_date']:
            dissection_date = str(individual['dissection_date'].date())
        return render('individual/infos.mako', extra_vars={
            '_id': individual['_id'],
            'species': individual['organism_classification']['_id'],
            'image_path':image_path,
            'sex': sex,
            'age': individual['adult'],
            'dissection_date': dissection_date,
            'measurements': individual['measures'],
            'measures_infos': measures_infos,
            'publications_list': publications_list,
            'country': individual['trapping_informations']['site']['country'],
            'province': individual['trapping_informations']['site']['province'],
            'region': individual['trapping_informations']['site']['region'],
            'surrounding_landscape': individual['trapping_informations']['site']['surrounding_landscape'],
            'latitude': individual['trapping_informations']['site']['coord_wgs']['dll_lat'],
            'longitude': individual['trapping_informations']['site']['coord_wgs']['dll_long'],
            'accuracy': individual['trapping_informations']['trap_accuracy'],
            'voucher': individual['voucher_barcoding'],
            'sequences': sequences,
            'api_key': google_map_api_key,
            'traits': traits,
            'physiologic_features': individual['physiologic_features'],
            'genotypes': individual['genotypes'],
            'title': "%s informations" % id.upper(),
        })

    def measurements(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        if not individual['voucher_barcoding'] and 'user' not in session:
            abort(401)
        species = individual['organism_classification']
        if not species:
            abort(404)
        measures_infos, publications_list, traits = self._measurements(individual, species)
        return render('individual/measurements.mako', extra_vars={
            '_id': individual['_id'],
            'species': individual['organism_classification']['_id'],
            'measures_infos': measures_infos,
            'publications_list': publications_list,
            'traits': traits,
            'title': "%s's measurements" % individual['_id'],
        })


    def _measurements(self, individual, species):
        ###### measures #######
        measures_infos = {}
        publications_list = []
        # one individual
        for measure in individual['measures']:
            if measure['trait'] not in measures_infos:
                measures_infos[measure['trait']] = {}
            measures_infos[measure['trait']][(None, individual['_id'], None)] = measure['value']
        publications_list.append((None, individual['_id'], None))
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
        if individual['measures']:
            tail_value = measures_infos["Tail (mm)"].get((None,id, None))
            if tail_value is not None and REGEXP_NUMBER.search(tail_value):
                tail_value = float(tail_value.replace(',', '.'))
            headnbody_value = measures_infos["Head & Body (mm)"].get((None,id, None))
            if headnbody_value is not None and REGEXP_NUMBER.search(headnbody_value):
                headnbody_value = float(headnbody_value.replace(',', '.'))
            if isinstance(tail_value, float) and isinstance(headnbody_value, float):
                if not "Tail / Head & Body (%)" in measures_infos:
                    measures_infos["Tail / Head & Body (%)"] = {}
                measures_infos["Tail / Head & Body (%)"][(None, id, None)] = int(tail_value/headnbody_value*100)
        traits = dict((int(i['_id']), i) for i in self.db.trait.find())
        ######## end measures #########
        return (measures_infos, publications_list, traits)


    def sequence(self, id, gene):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        sequence = self.db.sequence.find_one({'gene.$id':gene.lower(), 'individual.$id':id})
        if not sequence:
            abort(404)
        if not sequence['internet_display']:
            abort(404)
        fasta_name = "%s-%s" % ( id.upper(), "_".join(individual['organism_classification']['_id'].capitalize().split()))
        response.headers['Content-type'] = 'text/x-fasta'
        response.headers['Content-disposition'] = 'attachment; filename=%s.fasta' % fasta_name
        return ">%s\n%s\n" % (fasta_name.encode('utf-8'), sequence['sequence'].encode('utf-8'))

    def trapping(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        house_number = individual['trapping_informations']['site']['house']['number']
        if house_number is not None:
            house_number = math.pow(10, house_number)
        house_distance = individual['trapping_informations']['site']['house']['distance']
        if house_distance is not None:
            house_distance = math.pow(10, house_distance)
        path = os.path.join('data','static', 'trap lines pictures')
        file_path =  os.path.join('ceropath', 'public', path)
        server_path = os.path.join('/', path)
        upper_site_id = individual['trapping_informations']['site']['_id'].upper() 
        image_paths = []
        for file_name in os.listdir(file_path):
            if upper_site_id in file_name:
                image_paths.append(os.path.join(server_path, file_name))
        if house_number is None:
            house_number = 'unknown'
        else:
            house_number = int(house_number)
        if house_distance is None:
            house_distance = 'unknown'
        else:
            house_distance = int(house_distance)
        return render('individual/trapping.mako', extra_vars={
            '_id': individual['_id'],
            'species': individual['organism_classification']['_id'],
            'region': individual['trapping_informations']['site']['region'],
            'country': individual['trapping_informations']['site']['country'],
            'province': individual['trapping_informations']['site']['province'],
            'district': individual['trapping_informations']['site']['district'],
            'sub_district': individual['trapping_informations']['site']['sub_district'],
            'village': individual['trapping_informations']['site']['village'],
            'surrounding_landscape': individual['trapping_informations']['site']['surrounding_landscape'],
            'latitude': individual['trapping_informations']['site']['coord_wgs']['dll_lat'],
            'longitude': individual['trapping_informations']['site']['coord_wgs']['dll_long'],
            'house_presence': individual['trapping_informations']['site']['house']['presence'],
            'house_number': house_number,
            'house_distance': house_distance,
            'accuracy': individual['trapping_informations']['trap_accuracy'],
            'site': individual['trapping_informations']['site']['_id'],
            'eco_typology': individual['trapping_informations']['eco_typology'],
            'image_paths': image_paths,
            'api_key': google_map_api_key,
            'title': "%s trapping site informations" % id.upper(),
        })

    def module(self, id, name):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        return render('individual/module.mako', extra_vars={
            '_id': id,
            'species': individual['organism_classification']['_id'],
            'name': name,
            'title': "%s - %s" % (id.upper(), name),
        })

#    def parasites(self, id):
#        # XXX false
#        individual = self.db.individual.Individual.get_from_id(id)
#        if not individual:
#            abort(404)
#        if not individual['internet_display']:
#            abort(404)
#        rel_host_parasites_list = self.db.rel_host_parasite.find({'host.$id':individual['organism_classification']['_id']})
#        rel_host_parasites = {}
#        for rhp in rel_host_parasites_list:
#            try:
#                rel_host_parasites[rhp['_id']] = (rhp, self.db.publication.get_from_id(rhp['pubref']['$id']))
#            except:
#                rel_host_parasites[rhp['_id']] = (rhp, self.db.publication.get_from_id(rhp['pubref'].id))
#        return render('individual/parasites.mako', extra_vars={
#            'rel_host_parasites':rel_host_parasites,
#            '_id': id,
#        })
#
    def samples(self, id):
        individual = self.db.individual.Individual.get_from_id(id)
        if not individual:
            abort(404)
        if not individual['internet_display']:
            abort(404)
        return render('individual/samples.mako', extra_vars={
            '_id': id,
            'species': individual['organism_classification']['_id'],
            'samples': individual['samples'],
            'samples_owner': individual['samples_owner'],
            'title': "%s's samples" % id.upper(),
        })


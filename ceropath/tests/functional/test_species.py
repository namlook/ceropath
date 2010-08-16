from ceropath.tests import *

import logging
logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')

class TestSpeciesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='species', action='index'))
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            assert species['_id'].capitalize() in response, "%s not in response" % species['_id'].capitalize()
        for species in self.db.organism_classification.find({'internet_display': False, 'type':'mammal'}, fields=['_id']):
            assert species['_id'].capitalize() not in response, "%s in response" % species['_id'].capitalize()

    def test_show(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='show', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response
            assert "Taxonomic ranks" in response
            assert "General Informations" in response
            if not self.db.individual.find({'organism_classification.$id':species['_id']}).count():
                assert "This species wasn't sampling by Ceropath project" not in response, species

    def test_show_internet_display_false(self):
        for species in self.db.organism_classification.find({'internet_display': False, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='show', id=species['_id']), status=200)
            #if not self.db.individual.find({'organism_classification.$id':species['_id']}).count():
            assert "This species wasn't sampled by Ceropath project" in response, species

    def test_measurements_200(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='measurements', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response
            assert "CERoPath species measurements compare with literature data" in response

    def test_measurements_404_mammal(self):
        for species in self.db.organism_classification.find({'internet_display': False, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='measurements', id=species['_id']), status=404)

    def test_measurements_404_parasite(self):
        for species in self.db.organism_classification.find({'type':'parasite'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='measurements', id=species['_id']), status=404)

    def test_individuals(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='individuals', id=species['_id']), status=401)
        response = self.app.post(
            url=url(controller='login', action='submit'),
            params={
                'username': 'morand',
                'password': 'morand',
            }
        )
        response.session['user'] = 'morand'
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='individuals', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response
            for individual in self.db.individual.find({'organism_classification.$id': species['_id']}, fields=['_id', 'internet_display']):
                if individual['internet_display']:
                    assert individual['_id'].upper() in response, (species['_id'], individual['_id'])
                else:
                    assert individual['_id'].upper() not in response, (species['_id'], individual['_id'])

    def test_sampling_map(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='sampling_map', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response
            for individual in self.db.individual.find({'organism_classification.$id': species['_id']}, fields=['_id', 'internet_display', 'trapping_informations.site.$id']):
                if individual['internet_display']:
                    if individual['_id'].upper() not in response:
                        site = self.db.site.get_from_id(individual['trapping_informations']['site']['$id'])
                        assert not site['coord_wgs']['dll_lat'] or not site['coord_wgs']['dll_long'], (species['_id'], individual['_id'])
                    else:
                        assert individual['_id'].upper() in response, (species['_id'], individual['_id'])
                else:
                    assert individual['_id'].upper() not in response, (species['_id'], individual['_id'])

    def test_vouchers(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
            response = self.app.get(url(controller='species', action='vouchers', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response
            for individual in self.db.individual.find({'organism_classification.$id': species['_id'], 'voucher_barcoding':True}, fields=['_id', 'internet_display']):
                if individual['internet_display']:
                    assert individual['_id'].upper() in response, (species['_id'], individual['_id'])
                else:
                    assert individual['_id'].upper() not in response, (species['_id'], individual['_id'])

    def test_parasites(self):
        for species in self.db.organism_classification.find({'internet_display': True, 'type':'mammal'}, fields=['_id']):
#            try:
#                response = self.app.get(url(controller='species', action='parasites', id=species['_id']), status=200)
#            except:
#                print "============", species['_id']
#                continue
            response = self.app.get(url(controller='species', action='parasites', id=species['_id']), status=200)
            assert species['_id'].capitalize() in response, species
            rhps = self.db.rel_host_parasite.find({'host.$id':species['_id']}, fields=['parasite.$id'])
            if not rhps.count():
                assert "<table" not in response
            else:
                for rhp in rhps:
                    assert rhp['parasite']['$id'].capitalize() in response, (rhp, species['_id'])

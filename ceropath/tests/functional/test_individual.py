from ceropath.tests import *

class TestIndividualController(TestController):

    def test_show_voucher(self):
        for individual in self.db.individual.find({'voucher_barcoding':True}, fields=['_id', 'organism_classification.$id']):
            response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=200)
            assert individual['_id'].upper() in response
            assert individual['organism_classification']['$id'].capitalize() in response

    def test_show_non_voucher(self):
        for individual in self.db.individual.find({'voucher_barcoding':False, 'internet_display':True}, fields=['_id', 'organism_classification.$id']):
            response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=401)

    def test_show_non_voucher_with_auth(self):
        response = self.app.post(
            url=url(controller='login', action='submit'),
            params={
                'username': 'morand',
                'password': 'morand',
            }
        )
        response.session['user'] = 'morand'
        for individual in self.db.individual.find({'voucher_barcoding':False, "internet_display":True}, fields=['_id', 'organism_classification']):
            print individual
            if individual['organism_classification']:
                response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=200)
                assert individual['_id'].upper() in response
                assert individual['organism_classification'].id.capitalize() in response
            else:
                response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=404)

    def test_show_non_voucher_with_auth_not_internet_display(self):
        response = self.app.post(
            url=url(controller='login', action='submit'),
            params={
                'username': 'morand',
                'password': 'morand',
            }
        )
        response.session['user'] = 'morand'
        for individual in self.db.individual.find({'voucher_barcoding':False, "internet_display":False}, fields=['_id']):
            print individual
            response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=404)

    def test_show_non_voucher_non_internet_display(self):
        for individual in self.db.individual.find({'voucher_barcoding':False, 'internet_display':False}, fields=['_id', 'organism_classification.$id']):
            response = self.app.get(url(controller='individual', action='show', id=individual['_id']), status=404)


    def test_samples_voucher(self):
        for individual in self.db.individual.find({'voucher_barcoding':True}, fields=['_id', 'organism_classification.$id', 'samples']):
            response = self.app.get(url(controller='individual', action='samples', id=individual['_id']), status=200)
            assert individual['_id'].upper() in response
            assert individual['organism_classification']['$id'].capitalize() in response
            for sample in individual['samples']:
                assert sample['name'] in response
                for institute in sample['institute']:
                    assert institute.id in response
                for responsible in sample['responsible']:
                    assert responsible.id in response
                for project_institute in sample['project_institute']:
                    assert project_institute.id in response
                for project_responsible in sample['project_responsible']:
                    assert project_responsible.id in response
                assert sample['conservation_method'] or '' in response, (individual['_id'], sample['conservation_method'])

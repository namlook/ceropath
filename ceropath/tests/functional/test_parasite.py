from ceropath.tests import *

class TestParasiteController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='parasite', action='index'))
        for parasite in self.db.organism_classification.find({'internet_display': True, 'type':'parasite'}, fields=['_id']):
            assert parasite['_id'].capitalize() in response, "%s not in response" % parasite['_id'].capitalize()
        for parasite in self.db.organism_classification.find({'internet_display': False, 'type':'parasite'}, fields=['_id']):
            assert parasite['_id'].capitalize() not in response, "%s in response" % parasite['_id'].capitalize()

    def test_show_non_internet_display(self):
        for parasite in self.db.organism_classification.find({'internet_display': False, 'type':'parasite'}, fields=['_id']):
            response = self.app.get(url(controller='parasite', action='show', id=parasite['_id']), status=404)

    def test_show_with_internet_display(self):
        for parasite in self.db.organism_classification.find({'internet_display': True, 'type':'parasite'}, fields=['_id']):
            response = self.app.get(url(controller='parasite', action='show', id=parasite['_id']), status=200)
            assert parasite['_id'].capitalize() in response, "%s in response" % parasite['_id'].capitalize()

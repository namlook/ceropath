from ceropath.tests import *

class TestSpeciesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='species', action='index'))
        # Test response...

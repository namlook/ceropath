from ceropath.tests import *

class TestParasiteController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='parasite', action='index'))
        # Test response...

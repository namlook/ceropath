from ceropath.tests import *

class TestIndividualController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='individual', action='index'))
        # Test response...

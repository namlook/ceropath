from ceropath.tests import *

class TestInstituteController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='institute', action='index'))
        # Test response...

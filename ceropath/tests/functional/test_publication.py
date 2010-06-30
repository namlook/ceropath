from ceropath.tests import *

class TestPublicationController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='publication', action='index'))
        # Test response...

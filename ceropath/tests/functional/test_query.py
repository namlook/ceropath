from ceropath.tests import *

class TestQueryController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='query', action='index'))
        # Test response...

from ceropath.tests import *

class TestPipelineController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='pipeline', action='index'))
        # Test response...

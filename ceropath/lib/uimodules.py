from pylons.templating import render_mako as render
import helpers as h
from pylons import tmpl_context as c

class UIModule(object):

    def __call__(self, *args, **kwargs):
        return self.render(*args, **kwargs)

    def render(self, *args, **kwargs):
        raise NotImplementedError



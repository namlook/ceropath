"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons import config, session, request
from pylons.controllers.util import abort, redirect
from routes import url_for

class BaseController(WSGIController):

    connection = config['pylons.app_globals'].connection
    db = config['pylons.app_globals'].db

    # actions which require a login are listed below
    requires_auth_actions = []

    def __before__(self, action):
        if self.__class__.__name__ not in ['LoginController', 'ErrorController']:
            session['path_before_login'] = request.path_info
            session.save()
        if action in self.requires_auth_actions:
            if 'user' not in session:
                return redirect(url_for('login_show'))

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        return WSGIController.__call__(self, environ, start_response)

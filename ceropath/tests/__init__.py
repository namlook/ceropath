"""Pylons application test package

This package assumes the Pylons environment is already loaded, such as
when this script is imported from the `nosetests --with-pylons=test.ini`
command.

This module initializes the application via ``websetup`` (`paster
setup-app`) and provides the base testing objects.
"""
from unittest import TestCase

from paste.deploy import loadapp
import logging
from paste.script.appinstall import SetupCommand
from pylons import url, config
from routes.util import URLGenerator
from webtest import TestApp
from mongokit import Connection
from ceropath.model import register_models

import pylons.test

__all__ = ['environ', 'url', 'TestController']

# Invoke websetup with the current config file
#SetupCommand('setup-app').run([pylons.test.pylonsapp.config['__file__']])

environ = {}

class TestController(TestCase):

    def __init__(self, *args, **kwargs):
        wsgiapp = pylons.test.pylonsapp
        config = wsgiapp.config
        self.app = TestApp(wsgiapp)
        url._push_object(URLGenerator(config['routes.map'], environ))

        # db
        self.connection = Connection(
          host = config['db_host'],
          port = int(config['db_port']),
        )
        self.connection.register(register_models)
        self.db = self.connection[config['db_name']]

        TestCase.__init__(self, *args, **kwargs)

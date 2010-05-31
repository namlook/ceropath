"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

from mongokit import Connection
from ceropath.model import register_models
from pylons import config

class Globals(object):

    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))
        self.connection = Connection(
          host = config['db_host'],
          port = int(config['db_port']),
        )
        self.connection.register(register_models)
        self.db = self.connection[config['db_name']]


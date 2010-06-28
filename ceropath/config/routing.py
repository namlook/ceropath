"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('pipeline_index', '/pipeline', controller='pipeline', action='index')
    map.connect('pipeline_phyloexplorer', '/pipeline/phyloexplorer', controller='pipeline', action='phyloexplorer')
    map.connect('pipeline_config', '/pipeline/config', controller='pipeline', action='config')
    map.connect('pipeline_update_config', '/pipeline/config/update', controller='pipeline', action='update_config')

    # species
    map.connect('species_index', '/species', controller='species', action='index')
    map.connect('species_show', '/species/{id}', controller='species', action='show')
    map.connect('species_measurements', '/species/{id}/measurements', controller='species', action='measurements')
    map.connect('species_sampling_map', '/species/{id}/sampling_map', controller='species', action='sampling_map')
    map.connect('species_vouchers', '/species/{id}/vouchers', controller='species', action='vouchers')
    map.connect('species_individuals', '/species/{id}/individuals', controller='species', action='individuals')
    map.connect('species_module', '/species/{id}/{name}', controller='species', action='module')

    # individuals
    map.connect('individual_show', '/individual/{id}', controller='individual', action='show')
    map.connect('individual_trapping', '/individual/{id}/trapping', controller='individual', action='trapping')
    map.connect('individual_sequence', '/individual/{id}/sequence/{gene}', controller='individual', action='sequence')


    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map

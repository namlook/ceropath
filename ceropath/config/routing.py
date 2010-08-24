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

    # login
    map.connect('login_show', '/rdbsea/login', controller='login', action='show')
    map.connect('login_submit', '/rdbsea/login/submit', controller='login', action='submit')
    map.connect('login_logout', '/rdbsea/logout', controller='login', action='logout')

    # database
    map.connect('database_index', '/db', controller='database', action='index')
    map.connect('database_load', '/db/load', controller='database', action='load')
    map.connect('database_status', '/db/status', controller='database', action='status')

    # pipeline
    map.connect('pipeline_index', '/rdbsea/pipeline', controller='pipeline', action='index')
    map.connect('pipeline_result', '/rdbsea/pipeline/result', controller='pipeline', action='result')
    map.connect('pipeline_infos', '/rdbsea/pipeline/infos/{name}', controller='pipeline', action='infos')
    map.connect('pipeline_servesvg', '/rdbsea/pipeline/servesvg/{name}', controller='pipeline', action='servesvg')
    map.connect('pipeline_new', '/pipeline/config/new', controller='pipeline', action='new')
    map.connect('pipeline_create', '/pipeline/config/create', controller='pipeline', action='create')
    map.connect('pipeline_update', '/pipeline/config/update/{id}', controller='pipeline', action='update')
    map.connect('pipeline_list', '/pipeline/config/list', controller='pipeline', action='list')
    map.connect('pipeline_delete', '/pipeline/config/delete/{id}', controller='pipeline', action='delete')
    map.connect('pipeline_edit', '/pipeline/config/edit/{id}', controller='pipeline', action='edit')

    # query
    map.connect('query_index', '/rdbsea/query', controller='query', action='index')
    map.connect('query_run', '/rdbsea/query/run', controller='query', action='run')
    map.connect('query_expand', '/rdbsea/query/expand', controller='query', action='expand')
    map.connect('query_infos', '/rdbsea/query/infos', controller='query', action='infos')

    # institute
    map.connect('institute_show', '/rdbsea/institute/{id}', controller='institute', action='show')

    # species
    map.connect('species_index', '/rdbsea/species', controller='species', action='index')
    map.connect('species_filter', '/rdbsea/species/filter', controller='species', action='filter')
    map.connect('species_show', '/rdbsea/species/{id}', controller='species', action='show')
    map.connect('species_measurements', '/rdbsea/species/{id}/measurements', controller='species', action='measurements')
    map.connect('species_sampling_map', '/rdbsea/species/{id}/sampling_map', controller='species', action='sampling_map')
    map.connect('species_vouchers', '/rdbsea/species/{id}/vouchers', controller='species', action='vouchers')
    map.connect('species_individuals', '/rdbsea/species/{id}/individuals', controller='species', action='individuals')
    map.connect('species_parasites', '/rdbsea/species/{id}/parasites', controller='species', action='parasites')
    map.connect('species_module', '/rdbsea/species/{id}/{name}', controller='species', action='module')

    # individuals
    map.connect('individual_show', '/rdbsea/individual/{id}', controller='individual', action='show')
    map.connect('individual_measurements', '/rdbsea/individual/{id}/measurements', controller='individual', action='measurements')
    map.connect('individual_trapping', '/rdbsea/individual/{id}/trapping', controller='individual', action='trapping')
    map.connect('individual_sequence', '/rdbsea/individual/{id}/sequence/{gene}', controller='individual', action='sequence')
    map.connect('individual_parasites', '/rdbsea/individual/{id}/parasites', controller='individual', action='parasites')
    map.connect('individual_samples', '/rdbsea/individual/{id}/samples', controller='individual', action='samples')
    map.connect('individual_module', '/rdbsea/individual/{id}/{name}', controller='individual', action='module')

    # parasite
    map.connect('parasite_index', '/rdbsea/parasites', controller='parasite', action='index')
    map.connect('parasite_filter', '/rdbsea/parasite/filter', controller='parasite', action='filter')
    map.connect('parasite_show', '/rdbsea/parasite/{id}', controller='parasite', action='show')

    # publications
    map.connect('publication_show', '/rdbsea/publication/{id}', controller='publication', action='show')


    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map

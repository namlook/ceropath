"""Setup the ceropath application"""
import logging

import pylons.test

from ceropath.config.environment import load_environment

from ceropath.model import register_models
from mongokit import *
import os
import anyjson
from pprint import pprint

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup ceropath here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    db_name, host, port = conf.local_conf['db_name'], conf.local_conf['db_host'], conf.local_conf['db_port']
    con = Connection(host=host, port=int(port))
    con.register(register_models)
    #con.drop_database(db_name)
    db = con[db_name]

    pipeline_config = db.config.Pipeline()
    pipeline_config['programs'] = [
        {
            "path": u"/usr/bin",
            "name": u"sort",
            "input": u"STDIN",
            "options": u"-r",
            "output": None,
            "shell": False,
        },
        {
            "path": u"/usr/bin",
            "name": u"tr",
            "input": u"STDIN",
            "options": u"A-Z a-z",
            "output": None,
            "shell": False,
        }
    ]
    pipeline_config.save()
    documents_list = [
        'publication',
        'institute',
        'responsible',
        'organism_classification',
        'species_measurement',
        'individu',
        'gene',
        'primer',
        'sequence',
    ]

    for name in documents_list:#['gene', 'primer', 'sequence']:#documents_list:
        print ">>>>>>>", name, "<<<<<<<<<<"
        objs = anyjson.deserialize(open(os.path.join('data','json','%s.json' % name)).read())
        for obj in objs:
            #if name in ['organism_classification', 'species_measurement']:
            #    if name == 'species_measurement':
            #        pass
            #        pprint(obj)
            #        print
            #        pprint(db.organism_classification.get_from_id(obj['organism_classification']['$id']))
            #        print
            DocClass = getattr(db[name], "".join(i.capitalize() for i in name.split('_')))
            #pprint(obj)
            doc = DocClass.from_json(anyjson.serialize(obj).decode('utf-8', 'ignore'))
            doc.save()

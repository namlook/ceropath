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
    con.drop_database(db_name)
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

    for json_file in os.listdir('data/json'):
        print ">>>>>>>", json_file, "<<<<<<<<<<"
        objs = anyjson.deserialize(open(os.path.join('data','json','%s' % json_file)).read())
        for obj in objs:
            name = os.path.splitext(json_file)[0]
            DocClass = getattr(db[name], "".join(i.capitalize() for i in name.split('_')))
            pprint(obj)
            print
            doc = DocClass.from_json(anyjson.serialize(obj).decode('utf-8', 'ignore'))
            doc.save()

"""Setup the ceropath application"""
import logging

import pylons.test

from ceropath.config.environment import load_environment

from ceropath.model import register_models
from mongokit import *
import os
import sys
import anyjson
from pprint import pprint
from ceropath.lib.csv2json import csv2json


log = logging.getLogger(__name__)
#
#import re
#import math
#REGX_COI = re.compile('coi')
#REGX_CYTB = re.compile('cytb')
#REGX_PRIMER = re.compile('primer')
#REGX_16S = re.compile('16s')
#REGEXP_NUMBER = re.compile('^[\d\.,]+$')
#
#from statlib import stats
#
#def precalculate_ceropath_measurements(db, species_id):
#    query = {
#        'organism_classification.$id': species_id,
#        'adult':'adult',
#        'identification.type':{'$in':[REGX_COI, REGX_CYTB, REGX_PRIMER, REGX_16S]}
#    }
#    individuals = db.individual.find(query)
#    traits = {}
#    for individual in individuals:
#        for measure in individual['measures']:
#            trait = measure['trait']
#            if trait not in traits:
#                traits[trait] = []
#            if measure['value']:
#                traits[trait].append(measure['value'])
#    results = {}
#    for trait in traits:
#        values_list = [float(i.replace(',','.')) for i in traits[trait] if REGEXP_NUMBER.search(i)]
#        if trait not in results:
#            results[trait] = {}
#        if len(values_list) > 0:
#            results[trait]['mean'] = stats.mean(values_list)
#            if len(values_list) == 1:
#                results[trait]['sd'] = 0
#            else:
#                results[trait]['sd'] = stats.sterr(values_list)
#            results[trait]['n'] = len(values_list)
#            results[trait]['min'] = min(values_list)
#            results[trait]['max'] = max(values_list)
#        else:
#            results[trait]['mean'] = None
#            results[trait]['sd'] = None
#            results[trait]['n'] = None
#            results[trait]['min'] = None
#            results[trait]['max'] = None
#    results["Tail / Head & Body (%)"] = {'mean':0, 'n':0, 'sd':0, 'min':0, 'max':0}
#    if traits:
#        headnbody_values = [float(i.replace(',','.')) for i in traits["Head & Body (mm)"] if REGEXP_NUMBER.search(i)]
#        tail_values = [float(i.replace(',','.')) for i in traits["Tail (mm)"] if REGEXP_NUMBER.search(i)]
#        if len(headnbody_values) == len(tail_values):
#            headnbody_on_tail = 0
#            headnbody_on_tails = []
#            for index, val in enumerate(headnbody_values):
#                value = float(tail_values[index]) / float(headnbody_values[index])
#                headnbody_on_tails.append(value)
#                headnbody_on_tail += value
#            results["Tail / Head & Body (%)"]['mean'] = int((headnbody_on_tail/len(headnbody_values))*100)
#            results["Tail / Head & Body (%)"]['sd'] = 0
#            results["Tail / Head & Body (%)"]['n'] = len(headnbody_values)
#            results["Tail / Head & Body (%)"]['min'] = min(headnbody_on_tails)*100
#            results["Tail / Head & Body (%)"]['max'] = max(headnbody_on_tails)*100
#        else:
#            print species_id
#    return results
#
#def generate_species_measurements(db, species_id):
#    species_measurements = db.species_measurement.find(
#      {'organism_classification.$id': species_id}
#    )
#    results = {}
#    for species_measurement in species_measurements:
#        key = (species_measurement['pubref']['$id'], species_measurement['origin'])
#        if key not in results:
#            results[key] = {}
#        for measure in species_measurement['measures']:
#            trait = measure['trait']
#            if not trait in results[key]:
#                results[key][trait] = {}
#            if measure['value'] is not None:
#                measure['value'] = float(measure['value'].replace(',', '.'))
#            results[key][trait][species_measurement['type']] = measure['value']
#    return results

from ceropath.lib.precalculatemeasurments import pre_calculate_measurements

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

    bin_path = os.path.join(os.environ['PWD'], 'bin')
    pipeline_config = db.pipeline.Pipeline()
    pipeline_config['_id'] = u'Assigment in CERoPath reference tree'
    pipeline_config['programs'] = [
        {
            'name': u'Musle',
            "cmd": u"%s/muscle3.8.31_i86linux32 -in {{input}} -out {{output}}" % bin_path,
            'output_ext': u'afa',
            'use_stdin': False,
        },
        {
            'name': u'Musle 2',
            "cmd": u"%s/muscle3.8.31_i86linux32 -profile -in1 coi_cbgp.afa -in2 {{input}} -phyiout {{output}} -maxiters 1 -diags" % bin_path,
            'output_ext': u'phy',
            'use_stdin': False,
        },
        {
            'name': u'Dnadist options',
            "cmd": u'echo "{{input}}\\nF\\n{{output}}\\nD\\nY\\n"',
            'output_ext': u'mat',
            'use_stdin': False,
        },
        {
            'name': u'Dnadist',
            "cmd": u'%s/dnadist >> /tmp/log' % bin_path,
            'output_ext': None,
            "use_stdin": True,
        },
        {
            'name': u'BioNJ',
            "cmd": u'%s/BIONJ_linux {{input}} {{output}} >> /tmp/log' % bin_path,
            'output_ext': u'nwk',
            'use_stdin': False,
        },
        {
            'name': u'nwk2svg',
            "cmd": u'%s/nwk2svg.r {{input}} >> /tmp/log' % bin_path,
            'output_ext': u'svg',
            'use_stdin': False,
        },
        {
            'name': u'Return result',
            "cmd": u"cat {{input}}",
            'use_stdin': False,
            'output_ext': None,
        }
    ]
    pipeline_config.save()
    
#    print "Convert csv to json. Please wait..."
#    csv_path = os.path.join('data', 'csv')
#    yaml_path = os.path.join('data', 'yaml')
    json_path = os.path.join('data', 'json')
#    csv2json(csv_path, yaml_path, json_path)
#    print "...done"
#
    if 'iucn' not in os.listdir(os.path.join('ceropath', 'public')):
        os.mkdir(os.path.join('ceropath', 'public', 'iucn'))

    if 'data' not in os.listdir(os.path.join('ceropath', 'public')):
        os.mkdir(os.path.join('ceropath', 'public', 'data'))
    if 'static' not in os.listdir(os.path.join('ceropath', 'public', 'data')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static'))
    if 'alive animals' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'alive animals'))
    if 'chromatogram' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'chromatogram'))
    if 'measurements' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'measurements'))
    if 'primers' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'primers'))
    if 'trap lines pictures' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'trap lines pictures'))
    if 'vouchers skull pictures with measurements' not in os.listdir(os.path.join('ceropath', 'public', 'data', 'static')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'static', 'vouchers skull pictures with measurements'))

    if 'dynamic' not in os.listdir(os.path.join('ceropath', 'public', 'data')):
        os.mkdir(os.path.join('ceropath', 'public', 'data', 'dynamic'))
        
    if not 'json' in os.listdir('data'):
        os.mkdir(os.path.join('data', 'json'))
    for file_name in os.listdir(json_path):
        base, ext = os.path.splitext(file_name)
        print "Importing:", base
        os.system("mongoimport -d dbrsea -c %s --file %s.json" % (base, os.path.join(json_path, base)))


    print "pre-calculating measurements..."
    pre_calculate_measurements(db)
#    # XXX to remove
#    try:
#        db.organism_classification.OrganismClassification.find_one({'type':'mammal', 'internet_display':True})
#    except:
#        pass
#    try:
#        db.organism_classification.OrganismClassification.find_one({'type':'mammal', 'internet_display':True})
#    except:
#        pass
#
#    for species in db.organism_classification.OrganismClassification.find({'type':'mammal', 'internet_display':True}):
#        res = precalculate_ceropath_measurements(db, species['_id'])
#        measures_stats = {
#                'pubref': None,
#                'origin': None,
#                'measures':{}
#        }
#        for trait in res:
#            measures_stats['measures'][trait] = res[trait]
#        if res:
#            species['measures_stats'].append(measures_stats)
#        res = generate_species_measurements(db, species['_id'])
#        for (pubref, origin), values in res.iteritems():
#            species['measures_stats'].append({
#                'pubref': db.publication.Publication.get_from_id(pubref),
#                'origin': origin,
#                'measures': values,
#            })
#        species.save()
#    print "...done"
#    sys.exit()
#    print "importing json into the database %s. This may take a while..." % db.name
#    for name in json_allowed:
#        print 'processing :', name
#        objs = anyjson.deserialize(open(os.path.join(json_path,'%s.json' % name)).read())
#        DocClass = getattr(db[name], "".join(i.capitalize() for i in name.split('_')))
#        for obj in objs:
#            #if name in ['organism_classification', 'species_measurement']:
#            #    if name == 'species_measurement':
#            #        pass
#            #        pprint(obj)
#            #        print
#            #        pprint(db.organism_classification.get_from_id(obj['organism_classification']['$id']))
#            #        print
#            #pprint(obj)
#            doc = DocClass.from_json(anyjson.serialize(obj).decode('utf-8', 'ignore'))
#            doc.save()

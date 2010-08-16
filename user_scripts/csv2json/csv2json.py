import csv
#import anyjson
import json
from StringIO import StringIO
from pymongo import json_util
from pymongo.dbref import DBRef
import sys, os
import yaml
from pprint import pprint
from datetime import datetime
import codecs
from zipfile import ZipFile

def totimestamp(value):
    """
    convert a datetime into a float since epoch
    """
    import calendar
    return int(calendar.timegm(value.timetuple()) * 1000 + value.microsecond / 1000)

class DotExpandedDict(dict):
    """ 
    A special dictionary constructor that takes a dictionary in which the keys 
    may contain dots to specify inner dictionaries. It's confusing, but this 
    example should make sense. 

    >>> d = DotExpandedDict({'person.1.firstname': ['Simon'], \ 
          'person.1.lastname': ['Willison'], \ 
          'person.2.firstname': ['Adrian'], \ 
          'person.2.lastname': ['Holovaty']}) 
    >>> d 
    {'person': {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}} 
    >>> d['person'] 
    {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}} 
    >>> d['person']['1'] 
    {'lastname': ['Willison'], 'firstname': ['Simon']} 

    # Gotcha: Results are unpredictable if the dots are "uneven": 
    >>> DotExpandedDict({'c.1': 2, 'c.2': 3, 'c': 1}) 
    {'c': 1} 
    """
    # code taken from Django source code http://code.djangoproject.com/
    def __init__(self, key_to_list_mapping):
        for k, v in key_to_list_mapping.items():
            current = self
            bits = k.split('.')
            for bit in bits[:-1]:
               if bit.startswith('$'):
                   try:
                        bit = eval(bit[1:])
                   except:
                        raise EvalException('%s is not a python type' % bit[:1])
               current = current.setdefault(bit, {})
            # Now assign value to current position 
            last_bit = bits[-1]
            if last_bit.startswith('$'):
               try:
                    last_bit = eval(last_bit[1:])
               except:
                    raise EvalException('%s is not a python type' % last_bit)
            try:
                current[last_bit] = v
            except TypeError: # Special-case if current isn't a dict. 
                current = {last_bit: v}

def genjson(dict_list):
    results = []
    for i in dict_list:
        f = StringIO()
        json.dump(i, f, default=json_util.default)
        f.seek(0)
        results.append(f.read())
    return "\n".join(results)

def map_legend(legend, row):
    legend_map = {}
    for index, value in enumerate(row):
        legend_map[legend[index]] = value
    return legend_map

def split_synonyms(synonyms):
    for i in synonyms.split('[')[1:]:
        row = i.split(']')[0]
        synonyms = synonyms.replace(row, row.replace(';', ','))
    synonyms = synonyms.replace('<i>', '').replace('</i>', '').replace('<b>', '').replace('</b>', '')
    results = []
    for syn in synonyms.split(';'):
        syn = syn.strip()
        if syn:
            results.append(syn.split()[0].decode('utf-8', 'ignore'))
    return list(set(results))

def float_converter(value):
    if value is not None:
        if "," in value:
            value = value.replace(',', '.')
        return float(value)

def bool_converter(value):
    if value.lower() in ['yes', 'true', '1', 1]:
        return True
    return False

def int_converter(value):
    if value is not None:
        return int(value)

def dll_converter(value):
    if value is not None:
        return value.replace(',', '.')

def date_converter(value):
    if value is not None:
        return {'$date':totimestamp(datetime.strptime(value, "%d/%m/%Y"))}

def sex_checker(value):
    if value.lower() in ['f', 'm']:
        return value.lower()

def sanitize_article_id(value):
    return value.split(',')[0]

def filter_measurement_accuracy(value):
    if len(value.split(',')) > 1:
        return len(value.split(',')[1])
    return 0

def sample_no_converter(value):
    if value.lower() == 'no':
        return None
    return value

def process(csv_path, yaml_path, name, delimiter=';', quotechar='"'):
    config = yaml.load(open(os.path.join(yaml_path, '%s.yaml') % name).read())
    csv_lines = csv.reader(open(os.path.join(csv_path, '%s.csv') % name), delimiter=delimiter, quotechar='"')
    legend = csv_lines.next()
    for row in csv_lines:
        doc = {}
        dynamic_row = False
        for index, value in enumerate(row):
            assert len(legend) == len(row)
            field_name = legend[index]
            if dynamic_row:
                _field_name = field_name
                field_name = '_dynamic'
            if field_name in config:
                value = value.strip() or None
                if value:
                    if 'lower' in config[field_name] and not config[field_name]['lower']:
                        pass
                    else:
                        value = value.lower()
                    if 'filter' in config[field_name]:
                        value = eval(config[field_name]['filter'])(value)
                    if 'dbref' in config[field_name]:
                        if value is not None:
                            value = DBRef(collection=config[field_name]['dbref'], id=value, database='dbrsea')
                    if isinstance(value, str):
                        value = value.decode('utf-8', 'replace')
                if dynamic_row:# and 'field_name_target' in config[field_name]:
                    target = config['_dynamic']['field_name_target']
                    if 'embed' in config['_dynamic']:
                        embed = config['_dynamic']['embed']
                        if 'list' in config['_dynamic'] and config['_dynamic']['list']:
                            if not embed in doc:
                                doc[embed] = []
                            doc[embed].append({
                              config['_dynamic']['dbrsea']: value,
                              config['_dynamic']['field_name_target']: _field_name
                            })
                        else:
                            doc['%s.%s' % (embed, config['_dynamic']['dbrsea'])] = value
                            doc['%s.%s' % (embed, config['_dynamic']['field_name_target'])] = _field_name
                    else:
                        doc[config['_dynamic']['field_name_target']] = field_name
                        doc[config['_dynamic']['dbrsea']] = value
                else:
                    if 'list' in config[field_name] and config[field_name]['list']:
                        if value is None:
                            value = []
                        else:
                            if not isinstance(value, list):
                                value = [value]
                    doc[config[field_name]['dbrsea']] = value
                if 'last' in config[field_name]:
                    if config[field_name]['last']:
                        dynamic_row = True
        yield DotExpandedDict(doc)
    
def csv2json(csv_path, yaml_path, json_path, log_file):
    # Publication
    print "generating publications... "
    publications = dict((i['_id'],i) for i in process(csv_path, yaml_path, 't_literature_referens', delimiter=';'))
    open(os.path.join(json_path, 'publication.json'), 'w').write(genjson(publications.values()))

    # Institutes
    print "generating institutes..."
    institutes = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_lib_institutes'))
    open(os.path.join(json_path, 'institute.json'), 'w').write(genjson(institutes.values()))

    # Responsibles
    print "generating responsibles..."
    responsibles = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_lib_responsible'))
    open(os.path.join(json_path, 'responsible.json'), 'w').write(genjson(responsibles.values()))

    # Traits
    print "generating traits..."
    traits = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_lib_traits'))
    open(os.path.join(json_path, 'trait.json'), 'w').write(genjson(traits.values()))
 
    # OrganismClassification
    def get_organisms():
        organisms = process(csv_path, yaml_path, 't_species_systematic', delimiter=';')
        proceed_organisms = []
        for org in organisms:
            if org['_id'] is None:
                org['_id'] = '%s sp.' % org['taxonomic_rank']['genus']
            proceed_organisms.append(org)
        organisms = dict((i['_id'], i) for i in proceed_organisms)#process('t_species_systematic', delimiter='|'))
        synonyms = {}
        for i in process(csv_path, yaml_path, 't_species_synonyms'):
            if i['valid_name'] in organisms:
                if 'citations' not in organisms[i['valid_name']]:
                    organisms[i['valid_name']]['citations'] = []
                if 'synonyms' not in organisms[i['valid_name']]:
                    organisms[i['valid_name']]['synonyms'] = []
                organisms[i['valid_name']]['citations'].append({
                 'pubref': i['id_article'],
                  'name': i['species_article_name']
                })
                if i['species_article_name'] != i['valid_name']:
                    organisms[i['valid_name']]['synonyms'].append({
                     'pubref': i['id_article'],
                      'name': i['species_article_name']
                    })
                    synonyms[(i['species_article_name'], i['id_article'].id)] = i['valid_name']
            else:
                log_file.write("ERROR: %s is listed in t_species_synonyms as valid_name but was not found in t_species_systematic\n" % i['valid_name'])
        organism_classifications = []
        for name, org in organisms.iteritems():
            if org['_id'] is None: continue
            if not 'citations' in org:
                org['citations'] = []
            if not 'synonyms' in org:
                org['synonyms'] = []
            if org['type'] != 'parasite':
                org['type'] = u'mammal'
            for syn in org['msw3']['synonyms']:
                if syn == name:
                    org['citations'].append({'name':syn, 'pubref':DBRef(collection='publication', id='50999553', database='dbrsea')})
                else:
                    if org['id_msw3']:
                        org['synonyms'].append({'name':syn, 'pubref':DBRef(collection='publication', id='50999553', database='dbrsea')})
                        synonyms[(syn, '50999553')] = name
            del org['msw3']['synonyms']
            org['measures_stats'] = []
            organism_classifications.append(org)
        return organism_classifications, synonyms
    organism_classifications, synonyms = get_organisms()
    print "generating organism classifications..."
    open(os.path.join(json_path, 'organism_classification.json'), 'w').write(genjson(organism_classifications))
    organism_classifications = dict((i['_id'], i) for i in organism_classifications)
#    pprint(organisms['bandicota indica'])

    # SpeciesMeasurement
    species_synonyms = dict(((i['id_article'].id, i['species_article_name']), i) for i in process(csv_path, yaml_path, 't_species_synonyms'))
    #species_measurements = list(process(csv_path, yaml_path, 't_species_measurements'))
    species_measurements = []
    #pprint(list(process(csv_path, yaml_path, 't_species_measurements')))
    for measurement in process(csv_path, yaml_path, 't_species_measurements'):
        if species_synonyms.get((measurement['pubref'].id, measurement['species_article_name'])):
            measurement['organism_classification'] = DBRef(
              collection='organism_classification',
              id=species_synonyms[(measurement['pubref'].id, measurement['species_article_name'])]['valid_name'],
              database='dbrsea',
            )
            species_measurements.append(measurement)
        else:
            log_file.write("ERROR: %s was cited with %s in t_species_measurements but was not found in t_species_synonyms\n" % (
              measurement['species_article_name'], measurement['pubref'].id))
    print "generating species measurements..."
    open(os.path.join(json_path, 'species_measurement.json'), 'w').write(genjson(species_measurements))
    #for i in species_measurements:
        #if 'bandicota indica' in i['organism_classification'].id:
            #pprint(i)

    # Individuals
    individuals = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_individus'))
    #pprint(individus['r5415'])
    # add missing fields to individus:
    for _id in individuals:
        individuals[_id]['measures'] = []
        individuals[_id]['microparasites'] = []
        individuals[_id]['macroparasites'] = []
        individuals[_id]['samples'] = []
        individuals[_id]['genotypes'] = {}

    # Individual measurements
    for i in process(csv_path, yaml_path, 't_individus_measurements'):
        if i['_id'] in individuals:
            individuals[i['_id']]['measures'] = i['measures']
        else:
            log_file.write("ERROR: %s not found in t_individus but found in t_individus_measurements\n" % i['_id'])
#    pprint(individus['c0001'])

    # Individual microparasites
    #microparasites = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_individus_microparasites'))
    for i in process(csv_path, yaml_path, 't_individus_microparasites'):
        if i['_id'] in individuals:
            individuals[i['_id']]['microparasites'] = i['microparasites']
        else:
            log_file.write("ERROR: %s not found in t_individus but found in t_individus_microparasites\n" % i['_id'])
#    pprint(individus['c0001'])

    # Individual macroparasites
    for macroparasite in process(csv_path, yaml_path, 't_individus_macroparasites'):
        _id = macroparasite['individual_id']
        if _id in individuals:
            if not 'macroparasites' in individuals[_id]:
                individuals[_id]['macroparasites'] = []
            individuals[_id]['macroparasites'].append({'name':macroparasite['parasite'], 'quantity': macroparasite['quantity']})
        else:
            log_file.write("ERROR: %s not found in t_individus but found in t_individus_macroparasites\n" % _id)

    # Individual samples
    samples = dict((i['sample'], {'conservation_method': i['conservation method']}) for i in process(csv_path, yaml_path, 't_lib_samples'))
    #samples = dict((i['sample'], {'conservation_method': None}) for i in process(csv_path, yaml_path, 't_lib_samples'))
    for sample in process(csv_path, yaml_path, 't_samples_collection_management'):
        if sample['sample_name'] in samples:
            sample_name = sample['sample_name']
            if sample['institute']:
                sample_institute = sample['institute'].id
                if not sample_institute in samples[sample_name]:
                    samples[sample_name][sample_institute] = {}
                samples[sample_name][sample_institute]['name'] = sample_name
                samples[sample_name][sample_institute]['conservation_method'] = samples[sample_name]['conservation_method']
                if not 'responsible' in samples[sample_name][sample_institute]:
                    samples[sample_name][sample_institute]['responsible'] = []
                if sample['responsible'] not in samples[sample_name][sample_institute]['responsible']:
                    samples[sample_name][sample_institute]['responsible'].append(sample['responsible'])
                if not 'institute' in samples[sample_name][sample_institute]:
                    samples[sample_name][sample_institute]['institute'] = []
                if sample['institute'] not in samples[sample_name][sample_institute]['institute']:
                    samples[sample_name][sample_institute]['institute'].append(sample['institute'])
                if not 'project_responsible' in samples[sample_name][sample_institute]:
                    samples[sample_name][sample_institute]['project_responsible'] = []
                if sample['project_responsible'] not in samples[sample_name][sample_institute]['project_responsible']:
                    samples[sample_name][sample_institute]['project_responsible'].append(sample['project_responsible'])
                if not 'project_institute' in samples[sample_name][sample_institute]:
                    samples[sample_name][sample_institute]['project_institute'] = []
                if sample['project_institute'] not in samples[sample_name][sample_institute]['project_institute']:
                    samples[sample_name][sample_institute]['project_institute'].append(sample['project_institute'])
        else:
            print "----", sample
    for i in process(csv_path, yaml_path, 't_individus_samples'):
        if i['_id'] in individuals:
            for sample in i['samples']:
                if sample['institute']:
                    s = samples[sample['name']].get(sample['institute'].id)
                    if s:
                        individuals[i['_id']]['samples'].append(s)
        else:
            log_file.write("ERROR: %s not found in t_individus but found in t_individus_samples\n" % i['_id'])

    # Individual physiologic features
    for feature in process(csv_path, yaml_path, 't_individus_physiologic_features'):#physiologic_features:
        _id = feature['individual_id']
        if _id in individuals:
            individuals[_id]['physiologic_features'] = []
            individuals[_id]['physiologic_features'] = feature['physiologic_features']
        else:
            log_file.write("ERROR: %s not found in t_indivivus but found in t_individus_physiologic_features\n" % _id)

    # Individual genotyping
    for genotyping in process(csv_path, yaml_path, 't_individus_genotyping'):
        _id = genotyping['individual_id']
        if _id in individuals:
            individuals[_id]['genotypes'][genotyping['genotype']] = genotyping['value']
        else:
            log_file.write("ERROR: %s not found in t_indivivus but found in t_individus_genotyping\n" % _id)

    print "generating individuals..."
    open(os.path.join(json_path, 'individual.json'), 'w').write(genjson(individuals.values()))

    # Former Identifications
    former_identifications = list(process(csv_path, yaml_path, 't_individus_former_identifications'))
    open(os.path.join(json_path, 'former_identification.json'), 'w').write(genjson(former_identifications))

    # Microparasite
#    for i in process('t_individus_macroparasites'):
#        if i['host'].id == 'r4499':
#            pprint(i)


    # Gene
    print "generating genes..."
    genes = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_lib_genes'))
    open(os.path.join(json_path, 'gene.json'), 'w').write(genjson(genes.values()))

    # Sequence
    print "generating sequences..."
    sequences = list(process(csv_path, yaml_path, 't_individus_sequences'))
    open(os.path.join(json_path, 'sequence.json'), 'w').write(genjson(sequences))
    #for i in sequences:
    #    if i['individu'].id == 'c0001':
    #        pprint(i)

    # Primer
    primers = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_lib_primers'))
    for i in primers:
        primers[i]['remark'] = None
    print "generating primers..."
    open(os.path.join(json_path, 'primer.json'), 'w').write(genjson(primers.values()))

    # Site
    print "generating sites..."
    sites = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_sites'))
    open(os.path.join(json_path, 'site.json'), 'w').write(genjson(sites.values()))

    synonyms_with_pub = dict(((i['species_article_name'], i['id_article'].id), i['valid_name']) for i in process(csv_path, yaml_path, 't_species_synonyms'))
    synonyms = dict((i['species_article_name'], i['valid_name']) for i in process(csv_path, yaml_path, 't_species_synonyms'))
    # Macroparasite
    _macroparasites = process(csv_path, yaml_path, 't_species_hosts_parasites')
    macroparasites = []
    for macroparasite in _macroparasites:
        macroparasite['remark'] = None
        failed = False
        for _type in ['host', 'parasite']:
            if macroparasite[_type] not in synonyms:
                log_file.write("ERROR: %s is listed in t_species_hosts_parasites but was not found in t_species_synonyms\n" % macroparasite[_type])
                failed = True
            elif not synonyms_with_pub.get((macroparasite[_type], macroparasite['pubref'].id)):
                log_file.write("ERROR: %s was cited with %s in t_species_hosts_parasites but was not found in t_species_synonyms\n" % (
                  macroparasite[_type], macroparasite['pubref'].id))
                failed = True
            else:
                _id = synonyms_with_pub.get((macroparasite[_type], macroparasite['pubref'].id))
                if _id:
                    macroparasite[_type] = DBRef(collection='organism_classification', id=_id,  database='dbrsea')
                else:
                    failed = True
        if not failed:
            macroparasites.append(macroparasite)
    print "generating rel host parasites..."
    open(os.path.join(json_path, 'rel_host_parasite.json'), 'w').write(genjson(macroparasites))

if __name__ == "__main__":
    abs_path = os.path.abspath('.')
    csv_path = os.path.join(abs_path, 'csv')
    json_path = '.'
    yaml_path = os.path.join(abs_path, 'yaml')
    assert 'csv' in os.listdir(abs_path), 'csv directory not found'
    assert 'yaml' in os.listdir(abs_path), 'yaml directory not found'
    log_file = open('errors.log', 'w')
    csv2json(csv_path, yaml_path, json_path, log_file)
    log_file.close()
    myzip = ZipFile('json.zip', 'w')
    for filename in os.listdir(json_path):
        if '.json' in filename:
            myzip.write(filename)
    myzip.close()
    for filename in os.listdir(json_path):
        if '.json' in filename:
            os.remove(filename)

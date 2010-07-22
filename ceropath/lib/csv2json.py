
import csv
import anyjson
import sys, os
import yaml
from pprint import pprint
from mongokit import DotExpandedDict, totimestamp
from datetime import datetime
import codecs

def genjson(dict_list):
    return "\n".join(anyjson.serialize(i) for i in dict_list)

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

bool_converter = lambda x: True if x.lower() in ['yes', 'true', '1'] else False
int_converter = lambda x: int(x) if x is not None else None
dll_converter = lambda x: x.replace(',', '.') if x is not None else None
date_converter = lambda x: {'$date':totimestamp(datetime.strptime(x, "%d/%m/%Y"))} if x is not None else None
sex_checker = lambda x: x.lower() if x in ['f', 'm'] else None
sanitize_article_id = lambda x: x.split(',')[0]
filter_measurement_accuracy = lambda x: len(x.split(',')[1]) if len(x.split(',')) > 1 else 0
sample_no_converter = lambda x: None if x.lower() == 'no' else x

def process(csv_path, yaml_path, name, delimiter=';', quotechar='"'):
    config = yaml.load(open(os.path.join(yaml_path, '%s.yaml') % name).read())
    print name
    csv_lines = csv.reader(open(os.path.join(csv_path, '%s.csv') % name), delimiter=delimiter, quotechar='"')
    #csv_file = codecs.open(os.path.join(csv_path, '%s.csv') % name, 'r', 'utf-8').readlines()
    #csv_lines = ([j.strip(quotechar) for j in i.split(delimiter)] for i in csv_file)
    #csv_file = codecs.open(os.path.join(csv_path, '%s.csv') % name, 'r', 'utf-8')
    #csv_lines = UnicodeReader(csv_file, delimiter=delimiter)
    legend = csv_lines.next()
    for row in csv_lines:
        doc = {}
        for index, value in enumerate(row):
            assert len(legend) == len(row)
            field_name = legend[index]
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
                            value = {'$id':value, '$ref':config[field_name]['dbref'], '$db':'dbrsea'}
                    if isinstance(value, str):
                        value = value.decode('utf-8', 'replace')
                if 'field_name_target' in config[field_name]:
                    target = config[field_name]['field_name_target']
                    if 'embed' in config[field_name]:
                        embed = config[field_name]['embed']
                        if 'list' in config[field_name] and config[field_name]['list']:
                            if not embed in doc:
                                doc[embed] = []
                            doc[embed].append({
                              config[field_name]['dbrsea']: value,
                              config[field_name]['field_name_target']: field_name
                            })
                        else:
                            doc['%s.%s' % (embed, config[field_name]['dbrsea'])] = value
                            doc['%s.%s' % (embed, config[field_name]['field_name_target'])] = field_name
                    else:
                        doc[config[field_name]['field_name_target']] = field_name
                        doc[config[field_name]['dbrsea']] = value
                else:
                    if 'list' in config[field_name] and config[field_name]['list']:
                        if value is None:
                            value = []
                        else:
                            if not isinstance(value, list):
                                value = [value]
                    doc[config[field_name]['dbrsea']] = value
        yield DotExpandedDict(doc)
    
def csv2json(csv_path, yaml_path, json_path):
    # Publication
    print "generating publications..."
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
        organisms = process(csv_path, yaml_path, 't_species_systematic', delimiter='|')
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
                    synonyms[(i['species_article_name'], i['id_article']['$id'])] = i['valid_name']
            else:
                print "WARNING:", i['valid_name']
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
                    org['citations'].append({'name':syn, 'pubref':{'$db': 'dbrsea', '$id': '50999553', '$ref': 'publication'}})
                else:
                    org['synonyms'].append({'name':syn, 'pubref':{'$db': 'dbrsea', '$id': '50999553', '$ref': 'publication'}})
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
    species_measurements = list(process(csv_path, yaml_path, 't_species_measurements'))
    print "generating species measurements..."
    open(os.path.join(json_path, 'species_measurement.json'), 'w').write(genjson(species_measurements))
    #for i in species_measurements:
        #if 'bandicota indica' in i['organism_classification']['$id']:
            #pprint(i)

    # Individuals
    individuals = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_individus'))
    #pprint(individus['r5415'])
    # add missing fields to individus:
    for _id in individuals:
        individuals[_id]['measures'] = []
        individuals[_id]['microparasites'] = []

    # Former Identifications
    # XXX embed this in Individu ?
#    former_identifications = process('t_individus_former_identifications')
#    for i in former_identifications:
#        if i['individu']['$id'] == 'c0001':
#            pprint(i)

    # Individu measurements
    for i in process(csv_path, yaml_path, 't_individus_measurements'):
        if i['_id'] in individuals:
            individuals[i['_id']]['measures'] = i['measures']
#    pprint(individus['c0001'])

    # Individu microparasites
    #microparasites = dict((i['_id'], i) for i in process(csv_path, yaml_path, 't_individus_microparasites'))
    for i in process(csv_path, yaml_path, 't_individus_microparasites'):
        if i['_id'] in individuals:
            individuals[i['_id']]['microparasites'] = i['microparasites']
#    pprint(individus['c0001'])

    # Individual samples
    samples = dict((i['sample'], {'conservation_method': i['conservation method']}) for i in process(csv_path, yaml_path, 't_lib_samples'))
    #samples = dict((i['sample'], {'conservation_method': None}) for i in process(csv_path, yaml_path, 't_lib_samples'))
    pprint(samples)
    for sample in process(csv_path, yaml_path, 't_samples_collection_management'):
        if sample['sample_name'] in samples:
            sample_name = sample['sample_name']
            if sample['institute']:
                sample_institute = sample['institute']['$id']
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
            individuals[i['_id']]['samples'] = []
            for sample in i['samples']:
                if sample['institute']:
                    s = samples[sample['name']].get(sample['institute']['$id'])
                    if s:
                        print i['_id']
                        print '-'*len(i['_id'])
                        print s
                        individuals[i['_id']]['samples'].append(s)
    print "generating individuals..."
    open(os.path.join(json_path, 'individual.json'), 'w').write(genjson(individuals.values()))

    # RelHostParasite
#    for i in process('t_individus_macroparasites'):
#        if i['host']['$id'] == 'r4499':
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
    #    if i['individu']['$id'] == 'c0001':
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


    # Macroparasite
    _macroparasites = process(csv_path, yaml_path, 't_species_hosts_parasites')
    macroparasites = []
    for macroparasite in _macroparasites:
        macroparasite['remark'] = None
        failed = False
        if macroparasite['host']['$id'] not in organism_classifications:
            _id = synonyms.get((macroparasite['host']['$id'],macroparasite['pubref']['$id'])) 
            if _id:
                macroparasite['host']['$id'] = _id
            else:
                print "host>",  macroparasite['host']['$id']
                failed = True
        if macroparasite['parasite']['$id'] not in organism_classifications:
            _id = synonyms.get((macroparasite['parasite']['$id'],macroparasite['pubref']['$id'])) 
            if _id:
                macroparasite['parasite']['$id'] = _id
            else:
                print "parasite>", macroparasite['parasite']['$id']
                failed = True
        if not failed:
            macroparasites.append(macroparasite)
    print "generating rel host parasites..."
    open(os.path.join(json_path, 'rel_host_parasite.json'), 'w').write(genjson(macroparasites))

if __name__ == "__main__":
    csv_path = os.path.abspath(sys.argv[1])
    yaml_path = os.path.abspath(sys.argv[2])
    json_path = os.path.abspath(sys.argv[3])
    csv2json(csv_path, yaml_path, json_path)


import csv
import yaml
from pprint import pprint
from mongokit import DotExpandedDict, totimestamp
from datetime import datetime

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
date_converter = lambda x: totimestamp(datetime.strptime(x, "%d/%m/%Y")) if x is not None else None
sex_checker = lambda x: x.lower() if x in ['f', 'm'] else None
sanitize_article_id = lambda x: x.split(',')[0]

def process(name, delimiter=';'):
    config = yaml.load(open(os.path.join(yaml_path, '%s.yaml') % name).read())
    csv_file = csv.reader(open(os.path.join(csv_path, '%s.csv') % name), delimiter=delimiter, quotechar='"')
    legend = csv_file.next()
    for row in csv_file:
        doc = {}
        for index, value in enumerate(row):
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
    
if __name__ == "__main__":
    import anyjson
    import sys, os
    csv_path = os.path.abspath(sys.argv[1])
    yaml_path = os.path.abspath(sys.argv[2])
    json_path = os.path.abspath(sys.argv[3])
    # Publication
    publications = dict((i['_id'],i) for i in process('t_literature_referens'))
    open(os.path.join(json_path, 'publication.json'), 'w').write(anyjson.serialize(publications.values()))

    # Institutes
    institutes = dict((i['_id'], i) for i in process('t_lib_institutes'))
    open(os.path.join(json_path, 'institute.json'), 'w').write(anyjson.serialize(institutes.values()))

    # Responsibles
    responsibles = dict((i['_id'], i) for i in process('t_lib_responsible'))
    open(os.path.join(json_path, 'responsible.json'), 'w').write(anyjson.serialize(responsibles.values()))
 
    # OrganismClassification
    def get_organisms():
        organisms = process('t_species_systematic', delimiter='|')
        proceed_organisms = []
        for org in organisms:
            if org['_id'] is None:
                org['_id'] = '%s sp.' % org['taxonomic_rank']['genus']
            proceed_organisms.append(org)
        organisms = dict((i['_id'], i) for i in proceed_organisms)#process('t_species_systematic', delimiter='|'))
        synonyms = {}
        for i in process('t_species_synonyms'):
            if i['valid_name'] in organisms:
                if 'synonyms' not in organisms[i['valid_name']]:
                    organisms[i['valid_name']]['synonyms'] = []
                organisms[i['valid_name']]['synonyms'].append({
                 'pubref': i['id_article'],#{'$id': i['id_article'], '$ref':u'publication'},
                  'name': i['species_article_name']
                })
                if i['species_article_name'] != i['valid_name']:
                    synonyms[(i['species_article_name'], i['id_article']['$id'])] = i['valid_name']
            else:
                print "WARNING:", i['valid_name']
        organism_classifications = []
        for name, org in organisms.iteritems():
            if org['_id'] is None: continue
            if org['type'] == 'parasite':
                if not 'synonyms' in org:
                    org['synonyms'] = []
            else:
                if not 'synonyms' in org:
                    org['synonyms'] = []
                org['type'] = u'mammal'
            for syn in org['msw3']['synonyms']:
                org['synonyms'].append({'name':syn, 'pubref':{'$db': 'dbrsea', '$id': '50999553', '$ref': 'publication'}})
                if syn != name:
                    synonyms[(syn, '50999553')] = name
            del org['msw3']['synonyms']
            organism_classifications.append(org)
        return organism_classifications, synonyms
    organism_classifications, synonyms = get_organisms()
    open(os.path.join(json_path, 'organism_classification.json'), 'w').write(anyjson.serialize(organism_classifications))
    organism_classifications = dict((i['_id'], i) for i in organism_classifications)
#    pprint(organisms['bandicota indica'])

    # SpeciesMeasurement
    species_measurements = list(process('t_species_measurements'))
    open(os.path.join(json_path, 'species_measurement.json'), 'w').write(anyjson.serialize(species_measurements))
    #for i in species_measurements:
        #if 'bandicota indica' in i['organism_classification']['$id']:
            #pprint(i)

    # Individuals
    individuals = dict((i['_id'], i) for i in process('t_individus'))
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
    for i in process('t_individus_measurements'):
        if i['_id'] in individuals:
            individuals[i['_id']]['measures'] = i['measures']
#    pprint(individus['c0001'])

    # Individu microparasites
    microparasites = dict((i['_id'], i) for i in process('t_individus_microparasites'))
    for i in process('t_individus_microparasites'):
        if i['_id'] in individuals:
            individuals[i['_id']]['microparasites'] = i['microparasites']
#    pprint(individus['c0001'])
    open(os.path.join(json_path, 'individual.json'), 'w').write(anyjson.serialize(individuals.values()))

    # RelHostParasite
#    for i in process('t_individus_macroparasites'):
#        if i['host']['$id'] == 'r4499':
#            pprint(i)


    # Gene
    genes = dict((i['_id'], i) for i in process('t_lib_genes'))
    open(os.path.join(json_path, 'gene.json'), 'w').write(anyjson.serialize(genes.values()))

    # Sequence
    sequences = list(process('t_individus_sequences'))
    open(os.path.join(json_path, 'sequence.json'), 'w').write(anyjson.serialize(sequences))
    #for i in sequences:
    #    if i['individu']['$id'] == 'c0001':
    #        pprint(i)

    # Primer
    primers = dict((i['_id'], i) for i in process('t_lib_primers'))
    for i in primers:
        primers[i]['remark'] = None
    open(os.path.join(json_path, 'primer.json'), 'w').write(anyjson.serialize(primers.values()))

    # Site
    sites = dict((i['_id'], i) for i in process('t_sites'))
    open(os.path.join(json_path, 'site.json'), 'w').write(anyjson.serialize(sites.values()))


    # Macroparasite
    _macroparasites = process('t_species_hosts_parasites')
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
    open(os.path.join(json_path, 'rel_host_parasite.json'), 'w').write(anyjson.serialize(macroparasites))


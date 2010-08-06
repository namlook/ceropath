import re
import math
REGX_COI = re.compile('coi')
REGX_CYTB = re.compile('cytb')
REGX_PRIMER = re.compile('primer')
REGX_16S = re.compile('16s')
REGEXP_NUMBER = re.compile('^[\d\.,]+$')

from statlib import stats

def _precalculate_ceropath_measurements(db, species_id, use_moleculare_identification):
    query = {
        'organism_classification.$id': species_id,
        'adult':'adult',
    }
    if use_moleculare_identification:
        query['identification.type'] = {'$in':[REGX_COI, REGX_CYTB, REGX_PRIMER, REGX_16S]}
    individuals = db.individual.find(query)
    traits = {}
    individual_traits = {}
    for individual in individuals:
        for measure in individual['measures']:
            trait = measure['trait']
            if trait not in traits:
                traits[trait] = []
                individual_traits[trait] = {}
            if measure['value']:
                traits[trait].append(measure['value'])
                individual_traits[trait][individual['_id']] = measure['value']
    results = {}
    for trait in traits:
        values_list = [float(i.replace(',','.')) for i in traits[trait] if REGEXP_NUMBER.search(i)]
        if trait not in results:
            results[trait] = {}
        if len(values_list) > 0:
            results[trait]['mean'] = stats.mean(values_list)
            if len(values_list) == 1:
                results[trait]['sd'] = 0
            else:
                results[trait]['sd'] = stats.sterr(values_list)
            results[trait]['n'] = len(values_list)
            results[trait]['min'] = min(values_list)
            results[trait]['max'] = max(values_list)
        else:
            results[trait]['mean'] = None
            results[trait]['sd'] = None
            results[trait]['n'] = None
            results[trait]['min'] = None
            results[trait]['max'] = None
    results["Tail / Head & Body (%)"] = {'mean':0, 'n':0, 'sd':0, 'min':0, 'max':0}
    if traits:
        tail_on_head = []
        for individual_id, head_val in individual_traits['Head & Body (mm)'].iteritems():
            if individual_id in individual_traits['Tail (mm)']:
                head_val = head_val.replace(',', '.')
                tail_val = individual_traits['Tail (mm)'][individual_id].replace(',', '.')
                if REGEXP_NUMBER.search(head_val) and REGEXP_NUMBER.search(tail_val):
                    tail_on_head.append(float(tail_val)/float(head_val)*100)
        if tail_on_head:
            results["Tail / Head & Body (%)"]['mean'] = stats.mean(tail_on_head)
            results["Tail / Head & Body (%)"]['min'] = min(tail_on_head)
            results["Tail / Head & Body (%)"]['max'] = max(tail_on_head)
            results["Tail / Head & Body (%)"]['n'] = len(tail_on_head)
            results["Tail / Head & Body (%)"]['sd'] = 0
    return results

def _generate_species_measurements(db, species_id):
    species_measurements = db.species_measurement.find(
      {'organism_classification.$id': species_id}
    )
    results = {}
    for species_measurement in species_measurements:
        key = (species_measurement['pubref'].id, species_measurement['origin'], species_measurement['species_article_name'])
        if key not in results:
            results[key] = {}
        for measure in species_measurement['measures']:
            trait = measure['trait']
            if not trait in results[key]:
                results[key][trait] = {}
            if measure['value'] is not None:
                measure['value'] = float(measure['value'].replace(',', '.'))
            results[key][trait][species_measurement['type']] = measure['value']
    return results


def pre_calculate_measurements(db):
    print "pre-calculating measurements..."
    for species in db.organism_classification.OrganismClassification.find({'type':'mammal', 'internet_display':True}):
        res = _precalculate_ceropath_measurements(db, species['_id'], species['display_only_mol_identif'])
        measures_stats = {
                'pubref': None,
                'origin': None,
                'measures':{},
                'species_article_name': None,
        }
        for trait in res:
            measures_stats['measures'][trait] = res[trait]
        if res:
            species['measures_stats'].append(measures_stats)
        res = _generate_species_measurements(db, species['_id'])
        for (pubref, origin, species_article_name), values in res.iteritems():
            species['measures_stats'].append({
                'pubref': db.publication.Publication.get_from_id(pubref),
                'origin': origin,
                'measures': values,
                'species_article_name': species_article_name,
            })
        species.save()
    print "...done"
    #### end pre-caclulation #####


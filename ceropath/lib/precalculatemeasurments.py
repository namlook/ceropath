import re
import math
REGX_COI = re.compile('coi')
REGX_CYTB = re.compile('cytb')
REGX_PRIMER = re.compile('primer')
REGX_16S = re.compile('16s')
REGEXP_NUMBER = re.compile('^[\d\.,]+$')

from statlib import stats

def _precalculate_ceropath_measurements(db, species_id):
    query = {
        'organism_classification.$id': species_id,
        'adult':'adult',
        'identification.type':{'$in':[REGX_COI, REGX_CYTB, REGX_PRIMER, REGX_16S]}
    }
    individuals = db.individual.find(query)
    traits = {}
    for individual in individuals:
        for measure in individual['measures']:
            trait = measure['trait']
            if trait not in traits:
                traits[trait] = []
            if measure['value']:
                traits[trait].append(measure['value'])
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
        headnbody_values = [float(i.replace(',','.')) for i in traits["Head & Body (mm)"] if REGEXP_NUMBER.search(i)]
        tail_values = [float(i.replace(',','.')) for i in traits["Tail (mm)"] if REGEXP_NUMBER.search(i)]
        if len(headnbody_values) == len(tail_values):
            headnbody_on_tail = 0
            headnbody_on_tails = []
            for index, val in enumerate(headnbody_values):
                value = float(tail_values[index]) / float(headnbody_values[index])
                headnbody_on_tails.append(value)
                headnbody_on_tail += value
            results["Tail / Head & Body (%)"]['mean'] = int((headnbody_on_tail/len(headnbody_values))*100)
            results["Tail / Head & Body (%)"]['sd'] = 0
            results["Tail / Head & Body (%)"]['n'] = len(headnbody_values)
            results["Tail / Head & Body (%)"]['min'] = min(headnbody_on_tails)*100
            results["Tail / Head & Body (%)"]['max'] = max(headnbody_on_tails)*100
        else:
            print species_id
    return results

def _generate_species_measurements(db, species_id):
    species_measurements = db.species_measurement.find(
      {'organism_classification.$id': species_id}
    )
    results = {}
    for species_measurement in species_measurements:
        try:
            key = (species_measurement['pubref']['$id'], species_measurement['origin'])
        except:
            key = (species_measurement['pubref'].id, species_measurement['origin'])
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
    # XXX to remove
    try:
        db.organism_classification.OrganismClassification.find_one({'type':'mammal', 'internet_display':True})
    except:
        pass
    try:
        db.organism_classification.OrganismClassification.find_one({'type':'mammal', 'internet_display':True})
    except:
        pass

    for species in db.organism_classification.OrganismClassification.find({'type':'mammal', 'internet_display':True}):
        res = _precalculate_ceropath_measurements(db, species['_id'])
        measures_stats = {
                'pubref': None,
                'origin': None,
                'measures':{}
        }
        for trait in res:
            measures_stats['measures'][trait] = res[trait]
        if res:
            species['measures_stats'].append(measures_stats)
        res = _generate_species_measurements(db, species['_id'])
        for (pubref, origin), values in res.iteritems():
            species['measures_stats'].append({
                'pubref': db.publication.Publication.get_from_id(pubref),
                'origin': origin,
                'measures': values,
            })
        species.save()
    print "...done"
    #### end pre-caclulation #####


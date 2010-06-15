from core import Core
from publication import Publication

class OrganismClassification(Core):
    structure = {
        '_id': unicode, # bandicota indica #t_species_systematic/
        'id_msw3': unicode, # 100023 #t_species_systematic/
        'type': unicode, # mammal or parasite ? t_species_systematic/(host, typehost
        'taxonomic_rank':{
            'kingdom': unicode, #t_species_systematic/
            'phylum': unicode, #t_species_systematic/
            'class': unicode, #t_species_systematic/
            'order': unicode, #t_species_systematic/
            'suborder': unicode, #t_species_systematic/
            'infraorder': unicode, #t_species_systematic/
            'superfamily': unicode, #t_species_systematic/
            'family': unicode, #t_species_systematic/
            'subfamily': unicode, #t_species_systematic/
            'tribe': unicode, #t_species_systematic/
            'division': unicode, #t_species_systematic/
            'groups': unicode, #t_species_systematic/
            'genus': unicode, #t_species_systematic/
            'subgenus': unicode, #t_species_systematic/
            'species': unicode, #t_species_systematic/
            'subspecies': unicode, #t_species_systematic/
            'taxon_level': unicode, #t_species_systematic/
            'strain': unicode, #t_species_systematic/
            'extinct': bool,
        },
        'name':{
            'original': unicode, #t_species_systematic/
            'valid': bool, #t_species_systematic/
            'common':{
                unicode:unicode, # lang : valeur ['english', 'french', 'spanish', 'thai', 'tao', 'khmer']
            }, #t_species_systematic/
        },
        'reference':{
            'biblio':{
                'author': unicode,
                'date': unicode,
                'actual_date': unicode,
                'citation':{
                    'name': unicode,
                    'volume': unicode,
                    'issue': unicode,
                    'pages': unicode,
                    'type': unicode,
                },
            },
            'type':{
                'species': unicode,
                'locality': unicode,
            }
        },
        #'type_host': unicode,
        #'hosts': unicode,
        #'type_species': unicode,
        'msw3':{ # mammal species of the world
            #'type_locality': unicode, #t_species_systematic/
            'distribution': unicode, #t_species_systematic/
            'file': unicode, #t_species_systematic/
            'sort_order': unicode, #t_species_systematic/
            'display_order': unicode, #t_species_systematic/
            'status': unicode,
            'synonyms': [unicode], # not used, usefull for footprint.#t_species_systematic/
        },
        'internet_display': bool,#t_species_systematic/
        #'function': unicode, # permet de distinguer le parasite ou l'hote.
        'iucn':{
            'status': unicode, #t_species_systematic/
            'red_list_criteria_version': unicode, #t_species_systematic/
            'year_assessed': unicode, #t_species_systematic/
            'trend': unicode, #t_species_systematic/
            'id': unicode, #t_species_systematic/
        },
        'synonyms': [
            {'pubref': Publication, 'name':unicode},
        ],
    }
    use_autorefs = True

class Mammal(OrganismClassification):
    default_values = {'type':u'mammal'}

class Parasite(OrganismClassification):
    default_values = {'type': u'parasite'}

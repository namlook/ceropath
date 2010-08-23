from core import Core
from publication import Publication

class OrganismClassification(Core):
    collection_name = "organism_classification"
    structure = {
        '_id': unicode, # bandicota indica
        'id_msw3': unicode,
        'type': unicode, # mammal or parasite ?
        'internet_display': bool,
        'display_only_mol_identif': bool,
        'taxonomic_rank':{
            'kingdom': unicode,
            'phylum': unicode,
            'class': unicode,
            'order': unicode,
            'suborder': unicode,
            'infraorder': unicode,
            'superfamily': unicode,
            'family': unicode,
            'subfamily': unicode,
            'tribe': unicode,
            'division': unicode,
            'groups': unicode,
            'genus': unicode,
            'subgenus': unicode,
            'species': unicode,
            'subspecies': unicode,
            'taxon_level': unicode,
            'strain': unicode,
            'extinct': bool,
        },
        'name':{
            'original': unicode,
            'valid': bool,
            'common':{
                unicode:unicode, # lang : valeur ['english', 'french', 'spanish', 'thai', 'tao', 'khmer']
            },
        },
        'reference':{
            'biblio':{
                'author': unicode,
                'date': unicode,
                'author_date': unicode,
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
        'msw3':{ # mammal species of the world
            'distribution': unicode,
            'file': unicode,
            'sort_order': unicode,
            'display_order': unicode,
            'status': unicode,
        },
        'iucn':{
            'status': unicode,
            'red_list_criteria_version': unicode,
            'year_assessed': unicode,
            'trend': unicode,
            'id': unicode,
        },
        'citations': [
            {'pubref': Publication, 'name':unicode},
        ],
        'synonyms': [
            {'pubref': Publication, 'name':unicode},
        ],
        'measures_stats':[{
            'pubref': Publication,
            'origin': unicode,
            'measures':dict,# (mean +/- sd (nb_individu)) / (min - max)
            'species_article_name': unicode,
        }],
    }
    use_autorefs = True

    indexes = [
        {'fields':['internet_display']},
        {'fields':['taxonomic_rank.genus']},
        {'fields':['taxonomic_rank.family']},
    ]



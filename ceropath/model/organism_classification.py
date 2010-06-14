
class OrganismClassification(Core):
    structure = {
        '_id': unicode, # bandicota indica
        'id_msw3': unicode, # 100023
        'taxonomic_rank':
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
        },
        'extinct': bool,
        'name':{
            'original': unicode,
            'valid': unicode,
            'common':{
                unicode:unicode, # lang : valeur ['english', 'french', 'spanish', 'thai', 'tao', 'khmer']
            },
        },
        #'type_host': unicode,
        #'hosts': unicode,
        #'type_species': unicode,
        'type_locality': unicode,
        'distribution': unicode,
        'file': unicode,
        'sort_order': unicode,
        'synonyms': unicode, # not used, usefull for footprint.
        'display_order': unicode,
        'internet_display': unicode,
        #'function': unicode, # permet de distinguer le parasite ou l'hote.
        'status': unicode,
        'iucn':{
            'status': unicode,
            'red_List_criteria_version': unicode,
            'year_assessed': unicode,
            'trend': unicode,
            'id': unicode,
        },
        'synonyms':{
            [{'publication_reference': PublicationReference, 'name':unicode}]
        },
    }

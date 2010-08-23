
from mongokit import Document, IS
from datetime import datetime
from organism_classification import OrganismClassification
from institute import Institute
from responsible import Responsible
from site import Site

class Individual(Document):
    collection_name = "individual"
    structure = {
        '_id':unicode,
        'organism_classification': OrganismClassification,
        'sex': IS(u'f', u'm'),
        'adult': IS(u'adult', u'sub adult', u'youg adult', u'young', u'unknown'),
        'voucher_barcoding': bool,
        'skull_collection': bool,
        'dissection': bool,
        'dissection_date': datetime,
        'origin_remark': unicode,
        'identification':{
            'operator': unicode,
            'date': datetime,
            'type': unicode,
            'method': unicode,
            'molecular': unicode,
        },
        'trapping_informations':{
            'origin_how': unicode,
            'trap_accuracy': int,
            'site': Site,
            'eco_typology': {
                'remark': unicode,
                'low': unicode,
                'medium': unicode,
                'high': unicode,
            },
            'field_id': unicode,
            'alive': bool,
        },
        'samples_owner': unicode,
        'internet_display': bool,
        'dna':{
            'CBGP': bool,
            'extraction': bool,
            'extraction_CBGP': bool,
        },
        'mission':{
            'number': int,
            'remark': unicode,
        },
        'samples':[{
            'name':unicode,
            'conservation_method': unicode,
            'responsible': [Responsible],
            'institute':[Institute],
            'project_responsible': [Responsible],
            'project_institute':[Institute],
        }],
        'measures':[
            {'trait': unicode, 'value': unicode},
        ],
        'microparasites':[
            {'method': unicode, 'status': IS(u'positive', u'negative', u'undone')},
        ],
        'macroparasites':[
            {'name': unicode, 'quantity': unicode},
        ],
        'physiologic_features':[
            {'type': unicode, 'value': unicode},
        ],
        'genotypes':{unicode:unicode},
        'remark': unicode,
    }
    use_autorefs = True

    indexes = [
        {'fields':['internet_display']},
        {'fields':['organism_classification.$id'], 'check':False},
    ]

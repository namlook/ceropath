
from mongokit import Document, IS
from datetime import datetime
from organism_classification import OrganismClassification
from institute import Institute
from responsible import Responsible
from site import Site

class Individual(Document):
    structure = {
        '_id':unicode,#tu l'as appele 'individu' dans les tables que j'ai regarde avant pourquoi canger ?#t_individus/ID_individu
        'organism_classification': OrganismClassification, #t_individus.Valid_identification
        'sex': IS(u'f', u'm'), #t_individus/Sex
        'adult': IS(u'adult', u'sub adult', u'youg adult', u'young', u'unknown'), #t_individus/Adult
        'voucher_barcoding': bool, #t_individus/voucher_barcoding
        'skull_collection': bool, #t_individus/skull_collection
        'dissection': bool, #t_individus/dissection
        'dissection_date': datetime, #t_individus/dissection
        'origin_remark': unicode, #t_individus/origin_remark
        'identification':{
            'operator': unicode,
            'date': datetime,
            'type': unicode,
            'method': unicode,
            'molecular': unicode,
        },
        'trapping_informations':{
            'origin_how': unicode, #t_individus/Origin_how
            'trap_accuracy': int, #t_individus/Trap_accuracy
            'site': Site, # XXX Site, #t_individus/ID_site
            'eco_typology': { #EcoTypology,
                'remark': unicode,
                'low': unicode,
                'medium': unicode,
                'high': unicode,
            },
            'field_id': unicode, #t_individus/id_field
            'alive': bool, #t_individus/alive
        },
        'samples_owner': unicode, #t_individus/Samples_owner
        'internet_display': bool, #t_individus/internet_display
        'dna':{
            'CBGP': bool, #t_individus/dNA_CBGP
            'extraction': bool, #t_individus/dNA_extraction
            'extraction_CBGP': bool, #t_individus/dNA_extraction_CBGP
        },
        'mission':{
            'number': int, #t_individus/mission_number
            'remark': unicode, #t_individus/mission_remark
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
        'physiologic_features':[
            {'type': unicode, 'value': unicode},
        ],
        'genotypes':{unicode:unicode},
        'remark': unicode,
    }#t_lib_samples/sample
	#t_lib_responsibles/Responsible_name
    use_autorefs = True

    indexes = [
        {'fields':['organism_classification.$id'], 'check':False},
    ]

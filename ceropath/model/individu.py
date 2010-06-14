
from mongokit import Document
from datetime import datetime

class Individu(Document):
    structure = {
        '_id':unicode,
        'sex': IS(u'F', u'M'),
        'adult': IS(u'adult', u'subadult', u'youg'),
        'voucher_barcoding': bool,
        'skull_collection': bool,
        'date_of_dissection': datetime,
        'origin_remark': unicode,
        'trapping_informations':{
            'origin_how': unicode,
            'trap_accuracy': int,
            'site': Site,
            'eco_typology': EcoTypology,
            'id_field': unicode,
            'alive': bool,
        },
        'dissection': bool,
        'samples_owner': Responsible, 
        'internet_display': bool,
        'dna':{
            'cbgp': bool,
            'extraction': bool,
            'extraction_CBGP': bool,
        },
        'genotypage':{
            'drb': unicode,
            'microsat_nbmicrosat': int,
        },
        'mission':{
            'number': int,
            'remark': unicode,
        },
        'samples':[{'type':Sample, 'responsible':Responsible}],
    }


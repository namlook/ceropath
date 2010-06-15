
from mongokit import Document
from datetime import datetime
from organism_classification import Mammal

class Individu(Document):
    structure = {
        '_id':unicode,#tu l'as appelé 'individu' dans les tables que j'ai regardé avant pourquoi canger ?#t_individus/ID_individu
        'organism_classification': Mammal, #t_individus.Valid_identification
        'sex': IS(u'F', u'M'),#t_individus/Sex
        'adult': IS(u'adult', u'subadult', u'young'),#t_individus/Adult
        'voucher_barcoding': bool,#t_individus/voucher_barcoding
        'skull_collection': bool,#t_individus/skull_collection
        'dissection': bool,#t_individus/dissection
        'dissection_date': datetime,#t_individus/dissection
        'origin_remark': unicode,#t_individus/origin_remark
        'trapping_informations':{
            'origin_how': unicode,#t_individus/Origin_how
            'trap_accuracy': int,#t_individus/Trap_accuracy
            'site': Site,#t_individus/ID_site
            'eco_typology': {#EcoTypology,
                'remark': unicode,
                'low': unicode,
                'medium': unicode,
                'high': unicode,
            },
            'field_id': unicode,#t_individus/id_field
            'alive': bool,#t_individus/alive
        },
        'samples_owner': Responsible,#t_individus/Samples_owner
        'internet_display': bool,#t_individus/internet_display
        'dna':{
            'CBGP': bool,#t_individus/dNA_CBGP
            'extraction': bool,#t_individus/dNA_extraction
            'extraction_CBGP': bool,#t_individus/dNA_extraction_CBGP
        },
        #'genotypage':{
            # XXX TODO
            #'genotype': Genotyping, #j'ai créé une table t_lib_genotyping pour permettre de rajouter des génotypages avec des types différent (bol ou integer ou unicode...)
            ##'microsat_nbmicrosat': du coup je supprime ça
			#'value': 
        #},
        'mission':{
            'number': int,#t_individus/mission_number
            'remark': unicode,#t_individus/mission_remark
        },
        #'samples':[{'type':Sample, 'responsible':Responsible}], TODO
        'measures':[
            {'trait': unicode, 'value': unicode},
        ],
        'microparasite':[
            {'method': unicode, 'status': IS(u'positive', u'negative', 'undone')},
        ],
    }#t_lib_samples/sample
	#t_lib_responsibles/Responsible_name
    use_autorefs = True


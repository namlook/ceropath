
from mongokit import Document, IS
from datetime import datetime
from organism_classification import OrganismClassification
from responsible import Responsible

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
            'site': unicode, # XXX Site, #t_individus/ID_site
            'eco_typology': { #EcoTypology,
                'remark': unicode,
                'low': unicode,
                'medium': unicode,
                'high': unicode,
            },
            'field_id': unicode, #t_individus/id_field
            'alive': bool, #t_individus/alive
        },
        'samples_owner': Responsible, #t_individus/Samples_owner
        'internet_display': bool, #t_individus/internet_display
        'dna':{
            'CBGP': bool, #t_individus/dNA_CBGP
            'extraction': bool, #t_individus/dNA_extraction
            'extraction_CBGP': bool, #t_individus/dNA_extraction_CBGP
        },
        #'genotypage':{
            # XXX TODO
            #'genotype': Genotyping, #j'ai cree une table t_lib_genotyping pour permettre de rajouter des genotypages avec des types different (bol ou integer ou unicode...)
            ##'microsat_nbmicrosat': du coup je supprime ca
			#'value': 
        #},
        'mission':{
            'number': int, #t_individus/mission_number
            'remark': unicode, #t_individus/mission_remark
        },
        #'samples':[{'type':Sample, 'responsible':Responsible}], TODO
        'measures':[
            {'trait': unicode, 'value': unicode},
        ],
        'microparasites':[
            {'method': unicode, 'status': IS(u'positive', u'negative', u'undone')},
        ],
        'remark': unicode,
    }#t_lib_samples/sample
	#t_lib_responsibles/Responsible_name
    use_autorefs = True


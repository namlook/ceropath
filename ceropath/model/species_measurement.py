from organism_classification import OrganismClassification
from core import Core
from publication import Publication # XXX a enlever, c'est dans le core

class SpeciesMeasurement(Core):
    collection_name = "species_measurement"
    structure = {
        'organism_classification': OrganismClassification,
        'origin': unicode,
        'type': unicode,
		'measures':[{
            'trait': unicode, 
            'value': unicode,
        }],
        'remark': unicode,
        'pubref': Publication, # XXX a enlever, c'est dans le core
        'species_article_name': unicode,
    }
    indexes = [
        {'fields':[
            'organism_classification',
            #'pubref',
            'type'
        ], 'unique':True},
    ]
    use_autorefs = True

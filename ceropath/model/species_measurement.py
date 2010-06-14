
class SpeciesMeasurement(Core):
    structure = {
        'organism_classification': unicode, # OrganismClassification id
        'origin': unicode,
        'type': unicode,
        'value': unicode,
        'remark': unicode,
    }
    indexes = [
        {'fields':['publication_reference', 'type'], 'unique':True},
    ]

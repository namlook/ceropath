
class SpeciesMeasurement(Core):
    structure = {
        'organism_classification': OrganismClassification, # OrganismClassification id ##il faut traiter les synonimies
        'origin': unicode, #t_species_measurements/origin
        'type': unicode, #t_species_measurements/type
		'measures':[{
            'trait': unicode, 
            'value': unicode, #t_species_measurements/valeurs des variables de la table
        }],
        'remark': unicode, #t_species_measurements/remark
    }
    indexes = [
        {'fields':['organism_classification', 'pubref', 'type'], 'unique':True},
    ]

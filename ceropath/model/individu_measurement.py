
# XXX embed in Individu
class IndividuMeasurement(Core):
    structure = {
        'individu': Individu, #t_individus_measurements/ID_individu
        'measures':[{
            'type': unicode, #t_lib_traits/trait_name
            'value': unicode, #t_individus_measurements/valeurs des variables définies dans type
        }],
    }
    indexes = [
        {'fields':['individu', 'type'], 'unique':True},
    ]

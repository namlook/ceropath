
class IndividuMeasurement(Core):
    structure = {
        'individu': Individu,
        'type': unicode,
        'value': unicode,
    }
    indexes = [
        {'fields':['individu', 'type'], 'unique':True},
    ]

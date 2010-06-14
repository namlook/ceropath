
class PhysiologicFeatures(Core):
    structure = {
        'individu': Individu,
        'name': unicode,
        'value': unicode,
    }
    indexes = [
        {'fields':['individu', 'name'], 'unique':True},
    ]

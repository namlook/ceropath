
class FormerIdentification(Core):
    structure = {
        'individu': Individu,
        'valid_name': unicode,
        'date': datetime,
        'type': unicode,
        'operator': unicode,
        'remark': unicode,
    }
    indexes = [
        {'fields':['individu', 'valid'], 'unique':True},
    ]

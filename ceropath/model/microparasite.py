
class MicroparasiteIdentificationMethod(Document):
    structure = {
        'name': unicode,
    }

class Microparasite(Document):
    structure = {
        'individu': unicode,
        'method': MicroparasiteIdentificationMethod,
        'status': IS('positive', 'negative', 'undone'),
    }
    indexes = [
        {'fields':['individu', 'method'], 'unique':True},
    ]

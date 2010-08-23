from core import Core

class Trait(Core):
    collection_name = "trait"
    structure = {
        '_id': unicode, 
        'name': unicode, 
        'measurement_accuracy': int, 
    }

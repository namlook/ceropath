from core import Core
from individual import Individual
from organism_classification import OrganismClassification
from datetime import datetime

class FormerIdentification(Core):
    collection_name = "former_identification"
    structure = {
        'individual': Individual,
        # un individu peut-il avoir different organism_classification ? oui
        'organism_classification': OrganismClassification,
        'date': datetime,
        'type': unicode,
        'operator': unicode,
    }
    indexes = [
        {'fields':['individual', 'operator'], 'unique':True}, #XXX voir remark
    ]

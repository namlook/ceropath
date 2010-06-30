from core import Core
from organism_classification import OrganismClassification
from publication import Publication

class RelHostParasite(Core):
    structure = {
        'host': OrganismClassification,
        'parasite': OrganismClassification, 
        #'quantity': unicode,
        'country': unicode,
        'pubref': Publication
    }
    use_autorefs = True

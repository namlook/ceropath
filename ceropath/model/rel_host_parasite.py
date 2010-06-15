from core import Core

class RelHostParasite(Core):
    structure = {
        'host': OrganismClassification,
        'parasite': OrganismClassification, 
        'quantity': unicode,
        'country': Country,
    }
    use_autorefs = True

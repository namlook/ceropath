
class RelHostParasite(Core):
    structure = {
        'host': unicode, # OrganismClassification id
        'parasite': unicode, # OrganismClassification id
        'country': Country,
    }

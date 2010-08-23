from core import Core
from gene import Gene
from publication import Publication # XXX a supprimer, c'est dans core

class Primer(Core):
    collection_name = "primer"
    structure = {
        '_id': unicode,
        'sequence': unicode,
        'gene': Gene,
        'pubref': [Publication], # XXX a supprimer
    }
    use_autorefs = True

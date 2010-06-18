from core import Core
from gene import Gene
from publication import Publication # XXX a supprimer, c'est dans core

class Primer(Core):
    structure = {
        '_id': unicode,
        'sequence': unicode, #t_lib_primers/sequence "CCTACTCRGCCATTTTACCTATG"
        'gene': Gene,
        'pubref': [Publication], # XXX a supprimer
    }
    use_autorefs = True

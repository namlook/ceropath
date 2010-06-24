from core import Core
from individual import Individual
from gene import Gene
from primer import Primer

class Sequence(Core):
    structure = {
        'individu': Individual,# t_individus_sequences/ID_individu
        'gene': Gene,# t_individus_sequences/gene
        'sequence': unicode,# t_individus_sequences/sequence
        'operator': unicode,# t_individus_sequences/operator
        'primer':{
            'forward': Primer,# t_individus_sequences/forward
            'reverse': Primer,# t_individus_sequences/reverse
        },
        'chromatogram_link': unicode,# t_individus_sequences/chromatogram_link
        'length': int,# t_individus_sequences/lengh
        'accession_number': unicode, # id gen_bank # t_individus_sequences/Accession number
    }
    use_autorefs = True
    indexes = [
        {'fields':['individu', 'gene'], 'unique':True},
    ]

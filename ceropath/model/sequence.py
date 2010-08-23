from core import Core
from individual import Individual
from gene import Gene
from primer import Primer

class Sequence(Core):
    collection_name = "sequence"
    structure = {
        'individual': Individual,
        'gene': Gene,
        'sequence': unicode,
        'operator': unicode,
        'primer':{
            'forward': Primer,
            'reverse': Primer,
        },
        'chromatogram_link': unicode,
        'length': int,
        'accession_number': unicode,
        'internet_display': bool,
    }
    use_autorefs = True
    indexes = [
        {'fields':['individual', 'gene'], 'unique':True},
    ]

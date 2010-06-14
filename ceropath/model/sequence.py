
class Sequence(Core):
    structure = {
        'individu': Individu,
        'gene': Gene,
        'operator': unicode,
        'forward': unicode,
        'reverse': unicode,
        'sequence': unicode,
        'chromatogram_link': unicode,
        'length': int,
        'accession_number': unicode, # id gen_bank
    }
    indexes = [
        {'fields':['individu', 'gene'], 'unique':True},
    ]


class Sequence(Core):
    structure = {
        'individu': Individu,# t_individus_sequences/ID_individu
        'gene': Gene,# t_individus_sequences/gene
        'operator': unicode,# t_individus_sequences/operator
        'forward': unicode,# t_individus_sequences/forward
        'reverse': unicode,# t_individus_sequences/reverse
        'sequence': unicode,# t_individus_sequences/sequence
        'chromatogram_link': unicode,# t_individus_sequences/chromatogram_link
        'length': int,# t_individus_sequences/lengh
        'accession_number': unicode, # id gen_bank # t_individus_sequences/Accession number
    }
    indexes = [
        {'fields':['individu', 'gene'], 'unique':True},
    ]

from core import Core

class FormerIdentification(Core):
    # embed in individu
    # XXX Not used
    structure = {
        'individu': Individu,#t_individus_former_identifications/id_individu
        'organism_classification': OrganismClassification,#t_individus_former_identifications/Identification
        'date': datetime,#t_individus_former_identifications/date
        'type': unicode,#t_individus_former_identifications/Identification_type
        'operator': unicode,#t_individus_former_identifications/identification_operator
    }
    indexes = [
        {'fields':['individu', 'valid', 'operator'], 'unique':True}, #XXX voir remark
    ]
    # XXX un individu peut-il avoir different organism_classification ? oui

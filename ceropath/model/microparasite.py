
class MicroparasiteIdentificationMethod(Document):
    structure = {
        'name': unicode,#t_individus_microparasites/Hantavirus_IFA/Hantavirus_Western_Blot/Hantavirus_PCR_L/Hantavirus_PCR_S/Arenavirus_PCR_L/Ortopoxvirus_FP/Leptospirosis_PCR/Scrub_Thyphus_RTPCR/Ortopoxvirus_qPCR/Pneumosystis_PCR/Tripanosome/et tout ce qu'il pourront rajouter..........
    }

    ]
class Microparasite(Document):
    structure = {
        'individu': unicode,#t_individus_microparasites/id_individu
        'method': MicroparasiteIdentificationMethod,
        'status': IS('positive', 'negative', 'undone'),#t_individus_microparasites/valeurs des variables ci dessus dans la table microparasites
    }
    indexes = [
        {'fields':['individu', 'method'], 'unique':True},
    ]

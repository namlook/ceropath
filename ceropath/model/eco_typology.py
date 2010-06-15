
class EcoTypology(Core):
    structure = {
        'description': unicode, #t_individus/valeur de Typo_low_resolution ou Typo_medium_resolution ou Typo_high_resolution
        'resolution_level': IS('low', 'medium', 'high'),
    }
#à la place de nom je mettrais 'description'

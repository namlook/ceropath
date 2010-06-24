from individual import Individual

class Macroparasite(Core):
    # XXX PAS BESOIN ON MET TOUT DANS REL_HOST_PARASITE
    structure = {
        'host': Individual, #t_individus_macroparasites/id_individu
        'parasite': unicode, #t_individus_macroparasites/parasite_identification
        'quantity': unicode, #'value': unicode,#t_individus_macroparasites/value
    }
 #indexes = [
  #      {'fields':['individu', 'method'], 'unique':True},
   # ]
#je pense qu'il manque la clef primaire non ?
#j'ai bien compris là je peux ajouter autant de name de parasites que je veux ok ?

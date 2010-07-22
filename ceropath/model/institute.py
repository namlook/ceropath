from core import Core

class Institute(Core):
    structure = {
        '_id': unicode, # acronym
        'name': unicode, #t_lib_institutes/name
        'building': unicode, #t_lib_institutes/bulding
        'road': unicode, #t_lib_institutes/road
        'city': unicode, #t_lib_institutes/city
        'zip_code': unicode, #t_lib_institutes/zip_code
        'country': unicode, #t_lib_institutes/country
        'phone': unicode, #t_lib_institutes/phone
        'fax': unicode, #t_lib_institutes/fax
        #'email': unicode, #t_lib_institutes/e-mail
    }
#    use_autorefs = True
    #indexes = [
    #    {'fields':['name', 'acronym'], 'unique':True},
    #]

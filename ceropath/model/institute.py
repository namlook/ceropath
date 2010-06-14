
class Institute(Core):
    structure = {
        'name': unicode, #t_lib_institutes/name
        'acronym': unicode, #t_lib_institutes/Acronym
        'building': unicode, #t_lib_institutes/bulding
        'road': unicode, #t_lib_institutes/road
        'city': unicode, #t_lib_institutes/city
        'zip_code': unicode, #t_lib_institutes/zip_code
        'country': unicode, #t_lib_institutes/country
        'phone': unicode, #t_lib_institutes/phone
        'fax': unicode, #t_lib_institutes/fax
        'email': unicode, #t_lib_institutes/e-mail
    }
    #indexes = [
    #    {'fields':['name', 'acronym'], 'unique':True},
    #]

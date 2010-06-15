from institute import Institute
from core import Core

class Responsible(Core):
    structure = {
        'name': unicode, #t_lib_responsibles/Responsible_name
        'password': unicode, #t_lib_responsibles/Responsible_password
        'email': unicode, #t_lib_responsibles/Responsible_email
		'office': unicode, #t_lib_responsibles/responsible_office
        'office_phone': unicode, #t_lib_responsibles/
        'mobile_phone': unicode, #t_lib_responsibles/
        'fax': unicode, #t_lib_responsibles/
        'affiliation': Institute, #t_lib_responsibles/id_institute
    }
    use_autorefs = True

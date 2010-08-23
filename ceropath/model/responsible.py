from institute import Institute
from core import Core

class Responsible(Core):
    collection_name = "responsible"
    structure = {
        '_id': unicode, # name
        'password': unicode,
        'email': unicode,
		'office': unicode,
        'office_phone': unicode,
        'mobile_phone': unicode,
        'fax': unicode,
        'affiliation': Institute,
    }
    use_autorefs = True

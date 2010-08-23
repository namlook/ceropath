from core import Core

class Institute(Core):
    collection_name = "institute"
    structure = {
        '_id': unicode, # acronym
        'name': unicode,
        'building': unicode,
        'road': unicode,
        'city': unicode,
        'zip_code': unicode,
        'country': unicode,
        'phone': unicode,
        'fax': unicode,
    }

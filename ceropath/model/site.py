
from mongokit import Document

class Region(Document):
    structure = {'_id': unicode}

class Country(Document):
    structure = {'_id': unicode}

class Site(Core):
    structure = {
        '_id':unicode,
        'region': Region,
        'country':unicode, # TODO Doc
        'province':unicode, # TODO Doc
        'district':unicode, # TODO Doc
        'sub_district':unicode, # TODO Doc
        'village':unicode, # TODO Doc
        'sourrounding_landscape':unicode,
        'house':{
            'presence': bool,
            'number': int,
            'distance': int,
        },
        'coord_wgs':
            'utm_n':unicode,
            'utm_e':unicode,
            'dll_lat':unicode,
            'dll_long':unicode,
            'dms_lat':unicode,
            'dms_long':unicode,
            'elevation':unicode,
        },
        'ceropath_sites': bool,
        'id_correspondence': unicode, # former id from previous site
    }

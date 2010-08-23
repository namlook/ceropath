
from core import Core

class Site(Core):
    collection_name = "site"
    structure = {
        '_id':unicode,
        'region': unicode,
        'country':unicode,
        'province':unicode,
        'district':unicode,
        'sub_district':unicode,
        'village':unicode,
        'surrounding_landscape':unicode,
        'eco_typology': { #EcoTypology,
            'low': unicode,
            'medium': unicode,
            'high': unicode,
        },
        'house':{
            'presence': bool,
            'number': int,
            'distance': int,
        },
        'coord_wgs':{
            'utm_n' :unicode,
            'utm_e': unicode,
            'dll_lat': unicode,
            'dll_long': unicode,
            'dms_lat': unicode,
            'dms_long': unicode,
            'elevation': unicode,
        },
        'ceropath_sites': bool,
        'id_correspondence': unicode,
    }

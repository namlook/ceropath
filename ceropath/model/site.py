
#from mongokit import Document
from core import Core

#class Region(Document):
#    structure = {'_id': unicode}#t_sites/Region
#
#class Country(Document):
#    structure = {'_id': unicode}#t_sites/Country

class Site(Core):
    structure = {
        '_id':unicode, #t_sites/Id_site
        'region': unicode, #t_sites/Region
        'country':unicode, # TODO Doc#t_sites/Country
        'province':unicode, # TODO Doc#t_sites/Province
        'district':unicode, # TODO Doc#t_sites/District
        'sub_district':unicode, # TODO Doc#t_sites/Sub_district
        'village':unicode, # TODO Doc#t_sites/Village
        'surrounding_landscape':unicode, #t_sites/Sourrounding_landscape
        'eco_typology': { #EcoTypology,
            'low': unicode,
            'medium': unicode,
            'high': unicode,
        },
        'house':{
            'presence': bool ,#t_sites/House_presence
            'number': int, #t_sites/House_number
            'distance': int, #t_sites/House_distance
        },
        'coord_wgs':{
            'utm_n' :unicode, #t_sites/coord_WGS_UTM N
            'utm_e': unicode, #t_sites/coord_WGS_UTM E
            'dll_lat': unicode, #t_sites/Coord_WGS_DLL_Lat
            'dll_long': unicode, #t_sites/Coord_WGS_DLL_Long
            'dms_lat': unicode, #t_sites/coord_WGS_DMS_Lat
            'dms_long': unicode, #t_sites/coord_WGS_DMS_Lat
            'elevation': unicode, #t_sites/Elevation
        },
        'ceropath_sites': bool, #t_sites/CEROPATH_sites
        'id_correspondence': unicode, # former id from previous site#t_sites/ID_correspondance
    }

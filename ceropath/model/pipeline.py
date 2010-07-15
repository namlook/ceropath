
from mongokit import Document, IS

class Pipeline(Document):
    structure = {
        "_id":IS(u'pipeline'),
        "programs":[{
            "name": unicode,
            "use_stdin": bool,
            "cmd": unicode,
            "output_ext": unicode,
        }]
    }
    default_values = {'_id':u'pipeline'}


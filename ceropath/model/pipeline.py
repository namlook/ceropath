
from mongokit import Document, IS

class Pipeline(Document):
    structure = {
        "_id":IS(u'pipeline'),
        "programs":[{
            "shell": bool,
            "path": unicode,
            "name": unicode,
            "input": unicode,
            "options": unicode,
            "output": unicode,
        }]
    }
    default_values = {'_id':u'pipeline'}


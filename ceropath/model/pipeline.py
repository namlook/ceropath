
from mongokit import Document, IS

class Pipeline(Document):
    structure = {
        "_id": unicode,
        "programs":[{
            "name": unicode,
            "use_stdin": bool,
            "cmd": unicode,
            "output_ext": unicode,
        }]
    }
    def save(self, *args, **kwargs):
        if self['programs']:
            for prog in self['programs']:
                assert prog.get('name'), 'program name is required'
                assert prog.get('cmd'), 'cmd is required'
        super(Pipeline, self).save(*args, **kwargs)


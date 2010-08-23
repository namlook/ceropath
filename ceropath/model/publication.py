from mongokit import Document

class Publication(Document):
    collection_name = 'publication'
    structure = {
        '_id': unicode,
        'reference': unicode,
        'source': unicode,
        'remark': unicode,
        'link': unicode,
    }

from mongokit import Document

class Core(Document):
    structure = {
        'remark': unicode,
        'dbrsea': bool, # active actor of the project or only reference
        'publication_reference': [PublicationReference],
    }

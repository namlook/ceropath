from mongokit import Document
from publication import Publication

class Core(Document):
    structure = {
        'remark': unicode,
        #'dbrsea': bool, # active actor of the project or only reference
        #'pubref': [Publication],
    }
    use_autorefs = True

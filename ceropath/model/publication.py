
class PublicationReference(Document):
    structure = {
        '_id': unicode
        'reference': unicode, #t_literature_referens/Article_reference
        'source': unicode, # mamal species of the word #t_literature_referens/source
        'remark': unicode, #t_literature_referens/remark
    }

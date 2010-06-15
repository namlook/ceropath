
class Sample(Core):
    structure = {
        '_id': unicode,#t_lib_samples/sample
        'conservation_method':unicode,#t_lib_samples/Conservation method
    }
    
 indexes = [
        {'fields':['_id'', ''conservation_method'], 'unique':True},
    ]
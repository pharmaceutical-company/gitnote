import random 

import dulwich

def generate_id():
    id = '%05d' % random.randint(1, 99999)
#    if id in repos:
#        return generate_id():
    return id




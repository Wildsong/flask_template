
from .. import celery

@celery.task(name='add')
def Add(x,y):
    print("adding %d + %d" % (x,y))
    return x+y


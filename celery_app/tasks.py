
import os
from .extensions import celery

@celery.task(name='add')
def add(x,y):
    print("adding %d + %d" % (x,y))
    return x+y


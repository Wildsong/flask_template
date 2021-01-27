from .. import celery
import time

@celery.task(name='add')
def add(x,y):
    result = x + y
    time.sleep(5) # Add some delay to increase anticipation.
    return result

@celery.task(name='info')
def info():
    return "Details of your worker should go here. Stats or something."
    # I don't know what I can do to find them though.

@celery.task(name='log')
def log(msg):
    """ Just add two integers together to test the whole Celery thing. """
    print("log(%s)" % (msg))
    return msg


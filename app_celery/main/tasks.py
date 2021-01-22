from .. import celery

@celery.task(name='add')
def Add(x,y):
    result = x + y
    return result

@celery.task(name='info')
def Info():
    return "Details of your worker should go here. Stats or something."

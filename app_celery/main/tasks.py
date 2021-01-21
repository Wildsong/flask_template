from .. import celery

@celery.task(name='add')
def Add(x,y):
    print("Add(%d + %d)" % (x,y))
    return x+y

@celery.task(name='info')
def Info(x,y):
    print('Request: {0!r}'.format(self.request))
    return None
"""
    This is called from the celery CLI to start the worker, for example,

    celery -A celery_runner.py worker --loglevel=info
"""
import os
from celery_app import make_app
from celery_app.celery_factory import make_celery

env = os.environ.get('WEBAPP_ENV', 'dev')
flask_app = make_app('config.%sConfig' % env.capitalize())
celery = make_celery(flask_app)

"""
    This is called from the celery CLI to start the worker, for example,

    celery -A celery_runner.py worker --loglevel=info
"""
import os
from app_celery import create_app
from app_celery.celery_factory import make_celery
from version import version

config_name = os.environ.get('FLASK_ENV', 'default')
flask_app = create_app(config_name)
celery = flask_app.celery

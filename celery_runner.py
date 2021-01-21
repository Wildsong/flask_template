"""
    This is called from the celery CLI to start the worker, for example,

    celery -A celery_runner.py worker --loglevel=info
"""
import os
from app_celery import create_app
from app_celery.celery_factory import make_celery

flask_app = create_app(os.environ.get('WEBAPP_ENV', 'default'))
celery = create_celery(flask_app)

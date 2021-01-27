FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5002

# Set to None to make token last for entire session.
# https://flask-wtf.readthedocs.io/en/stable/config.html?highlight=csrf#
WTF_CSRF_TIME_LIMIT=None

CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0


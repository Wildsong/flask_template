"""
Start me with

    FLASK_APP=start_celery_app flask run

"""
import os
from unittest.loader import TestLoader
from app_celery import create_app
from version import version

app = create_app(os.environ.get('FLASK_ENV', 'default'))

# You need this if you use authentication
# #@app.shell_context_processor
#def make_shell_context():
#    return dict(db=db, User=User, Role=Role)    

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
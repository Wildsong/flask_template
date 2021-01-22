"""
Start me with

    FLASK_APP=start_simple_app flask run

"""
import os
from unittest.loader import TestLoader
from app_simple import create_app
from version import version

app = create_app(os.environ.get('FLASK_ENV', 'default'))

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


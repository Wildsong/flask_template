"""
Start me with

    FLASK_APP=start_celery_app flask run

"""
import os
from app_celery import create_app
from version import version

app = create_app(os.environ.get('FLASK_ENV', 'default'))

#@app.shell_context_processor
#def make_shell_context():
#    return dict(db=db, User=User, Role=Role)    

if __name__ == '__main__':
    print("version:", version)
    app.run(host=os.environ.get('FLASK_HOST'), port=os.environ.get('FLASK_PORT'))

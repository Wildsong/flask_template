import logging
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from .flask_celery import make_celery

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)


def page_not_found(error):
    return render_template('404.html'), 404


def create_app(configuration):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """
    app = Flask(__name__)
    app.config.from_object(configuration)
    bootstrap.init_app(app)
    debug_toolbar.init_app(app)

    celery = make_celery(app)
    
    # Load blueprints
    from .main import create_module as main_create_module

    main_create_module(app)
    app.register_error_handler(404, page_not_found)
    return app

# That's all!

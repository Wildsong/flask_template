import os
import logging
from flask import Flask, render_template
from config import config

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)


def page_not_found(error):
    return render_template('404.html'), 404


def create_app(config_name):
    """
    A flask app factory
    Arguments:
        config_name: key for the config dict
    """

    environment = os.environ.get('FLASK_ENV', 'production')

    app = Flask(__name__)
    app.config.from_object(config[environment])

    config[environment].init_app(app) 
    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    #assets_env.init_app(app)

    # Add routes and custom error pages
     
    # Load blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.register_error_handler(404, page_not_found)
    return app

# That's all!


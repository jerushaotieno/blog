from flask import Flask, app
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy


# Initializing Flask Extensions
bootstrap = Bootstrap()  

db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initialize db
    db.init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
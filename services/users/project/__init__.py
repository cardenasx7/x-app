# services/users/project/__init__.py


import os  # nuevo

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # nuevo

# instanciando la db
db = SQLAlchemy()  # nuevo


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app

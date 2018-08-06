import os

from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# top level globals, for importing in other modules
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """Simple factory pattern to avoid cyclic imports"""
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS', 'config.AppConfig')
    app.config.from_object(app_settings)

    # initialize application components
    app.secret_key = os.environ['APP_SECRET_KEY']

    db.init_app(app)
    ma.init_app(app)

    # register blueprints
    from api.views import api_blueprint
    app.register_blueprint(api_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5090, debug=True)

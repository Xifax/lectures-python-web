# app/errors/__init__.py
from flask import Blueprint

blueprint = Blueprint('errors', __name__)

from app.errors import handlers



# app/errors/handlers.py
from flask import render_template
from app import db
from app.errors import blueprint

@blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404



# app/__init__.py
app = Flask(__name__)

from app.errors import blueprint as errors_blueprint
app.register_blueprint(errors_blueprint)

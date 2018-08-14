# api/views.py

from flask import render_template, Blueprint, jsonify

from models import Company, CompanySchema

api_blueprint = Blueprint('api', __name__,)

companies_schema = CompanySchema(many=True)

@api_blueprint.route('/')
def home():
    companies = Company.query.all()
    result = companies_schema.dump(companies)
    return jsonify(result.data)
    # return 'Hello there guys!'

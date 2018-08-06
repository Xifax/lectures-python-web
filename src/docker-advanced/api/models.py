import os

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from app import db, ma


class Company(db.Model):
    """
    Example Company table
    """
    __tablename__ = 'drug_companies'

    id = Column(Integer, primary_key=True)
    company = Column(String(250))
    ceo = Column(String(250))
    drug = Column(String(500))
    slogan = Column(String(250))
    email = Column(String(250), unique=True)
    image = Column(String(250))

class CompanySchema(ma.Schema):
    class Meta:
        # expose those fields to api
        fields = ('company', 'ceo', 'drug', 'slogan', 'email', 'image') 

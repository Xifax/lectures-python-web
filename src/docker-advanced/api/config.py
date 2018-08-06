import os

from sqlalchemy import create_engine

class AppConfig:
    user = os.environ['POSTGRES_USER']
    pwd = os.environ['POSTGRES_PASSWORD']
    db = os.environ['POSTGRES_DB']
    host = 'db'
    port = '5432'
    # engine = create_engine(
    #         'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
    #         )
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)


from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
from flask_restplus import Api
from db import db
from config import config
import os

ENVIRONMENT = os.getenv('PYTHON_ENVIRONMENT')

POSTGRES_USER = config['Postgres']['username']
POSTGRES_PW = config['Postgres']['password']
POSTGRES_URL = config['Postgres']['url']
POSTGRES_DB = config['Postgres']['db']
POSTGRES_PORT = config['Postgres']['port']
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,port=POSTGRES_PORT,db=POSTGRES_DB)
app = Flask(__name__, static_url_path='')
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'sql-key-muy-secreta'

api = Api(
    app,
    version=config['AppSettings']['version'],
    description=config['AppSettings']['description'],
    title=config['AppSettings']['title']
)

api.namespaces = []

@app.before_first_request
def create_db():
    db.create_all()
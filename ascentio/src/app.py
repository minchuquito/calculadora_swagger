import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import argparse
from api import api, app

from resources.calculos import Calculos

from db import db
from flask import Flask
from config import config

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, host=config['host'], port=config['port'])
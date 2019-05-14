# Import logging for showing what occurs
import logging
# Import Flask for flask app object
from flask import Flask
# Import Flask appbuilder functions to create the appbuilder object
from flask_sqlalchemy import SQLAlchemy


"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# Create flask app object
app = Flask(__name__)

# Get Configs from config.py
app.config.from_object('config')

# Create Database object frmo flask app object
db = SQLAlchemy(app)

# Import views
import app.views
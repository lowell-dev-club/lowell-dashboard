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

# Add configurations to app
app.config.from_pyfile('config.py', silent=True)

# Create Database object from flask app object
# use the function db.create_all() to make the db
db = SQLAlchemy(app)

# Import views
from app import views
from app import initializedb
initializedb.initializedb()

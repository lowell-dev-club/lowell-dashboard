# Import logging for showing what occurs
import logging

# Import Flask for flask app object
from flask import Flask

# Import Flask modules to create objects for our app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

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
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)

# Import views
from app import views
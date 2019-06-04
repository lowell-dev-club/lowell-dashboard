# Import logging for showing what occurs
import logging

# Import Flask for flask app object
from flask import Flask

# Import Flask modules to create objects for our app
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
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
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Create mail object from flash app object
mail = Mail(app)

# importing all the models and initializing them
from app.models import *
db.create_all()

# Import views
from app import views
'''
Put config materials here
Ex: database configurations, keys, etc.
'''

from app import secret
import os

'''
To create a secret key run the program
import secrets
secrets.token_hex(16)
'''

'''
Config class
'''
class Config(object):
	basedir = os.path.abspath(os.path.dirname(__file__))

	SECRET_KEY = secret.SECRET_KEY
	SECURITY_PASSWORD_SALT = secret.SECRET_SALT
	RECAPTCHA_PUBLIC_KEY = secret.RECAPTCHA_SITE_KEY
	RECAPTCHA_PRIVATE_KEY = secret.RECAPTCHA_SECRET_KEY
	RECAPTCHA_USE_SSL = False
	RECAPTCHA_OPTIONS = {'theme':'white'}
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	        'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	'''
	Configurations for the email api
	Orginally from lowell-dashboard v1
	'''
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'LowellHelpForum@gmail.com'
	MAIL_PASSWORD = secret.EMAIL_PASS
	MAIL_DEFAULT_SENDER = 'Lowell Help Forum <LowellHelpForum@gmail.com>'
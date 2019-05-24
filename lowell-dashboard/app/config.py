'''
Put config materials here
Ex: database configurations, keys, etc.
'''

from app import secret

'''
To create a secret key run the program
import secrets
secrets.token_hex(16)
'''

SECRET_KEY = secret.SECRET_KEY
SQLALCHEMY_DATABASE_URI = 'postgresql://'

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
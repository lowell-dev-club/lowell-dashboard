from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

'''
Create a registation form
'''


class RegistrationForm(FlaskForm):
    '''
    Create a string field and call it username
    Field can't be empty, length of the string must be between 2 and 20 characters
    '''
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    '''
	Create a string field and call it email
	This field will accept email and use the Email validator to make sure it's a email
	'''
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    '''
	Create a string field and call it password
	This field will take in a string for the password
	'''
    password = PasswordField('Password', validators=[DataRequired()])
    '''
	Create a string field and call it confirm password
	This field will take a string and make sure the passwords are matching
	'''
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    '''
	Create a submit button
	'''
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')


'''
Create a registation form
'''


class LoginForm(FlaskForm):
    '''
    Create a string field and call it email
    This field will accept email and use the Email validator to make sure it's a email
    '''
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    '''
	Create a string field and call it password
	This field will take in a string for the password
	'''
    password = PasswordField('Password', validators=[DataRequired()])
    '''
	Create boolean field so we can know if the user wants the browser to rember them
	'''
    remember = BooleanField('Remember Me')
    '''
	Create a submit button
	'''
    submit = SubmitField('Login')

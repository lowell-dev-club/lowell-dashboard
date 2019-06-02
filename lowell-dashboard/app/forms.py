from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf import FlaskForm
from app.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


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
            raise ValidationError(
                'That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already being used. Please choose a different one')

'''
Create a activation confirmation form
'''


class ActivationConfirmation(FlaskForm):
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
    Create a submit button
    '''
    submit = SubmitField('Submit')


'''
Create a login form
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


class UpdateAccountForm(FlaskForm):
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
    Create a file field that will accept a file
    The validator for this field is a file allower that only accepts files with extensions of jpg and png
    '''
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    '''
    Create a submit button
    '''
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is already being used. Please choose a different one')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

from app import app
from flask import render_template, request, make_response, redirect, session, url_for, send_file, flash
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.html')	

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	if form.email.data == 'a@a.com' and form.password.data == 'pass':
    		flash('You have been logged in!', 'success')
    		return redirect(url_for('home'))
    	else:
    		flash('Login Unseccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

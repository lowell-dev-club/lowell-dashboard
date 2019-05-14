from app import app
from flask import render_template, request, make_response, redirect, session, url_for, send_file

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
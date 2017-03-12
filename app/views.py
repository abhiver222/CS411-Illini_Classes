from app import app
from flask import render_template, request, session, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    """
    route renders the landing page
    """
    return render_template('landing.html')

@app.route('/login', methods=['POST'])
def search():
    print request.form('cname')
    return render_template('landing.html')
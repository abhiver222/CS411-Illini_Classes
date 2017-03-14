from app import app
from flask import render_template, request, session, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    """
    route renders the landing page
    """
    return render_template('landing.html')

@app.route('/', methods=['POST','GET'])
def search():
    print request.form['cname']
    if request.method == 'POST':
        return render_template('course.html')
        # return redirect(url_for('index'))
    return "what"

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text
from app import app
from flask import render_template, request, session, flash, redirect, url_for
from app.data.query import Query

@app.route('/')
@app.route('/index')
def index():
    """
    route renders the landing page
    """
    print " in index "
    return render_template('landing.html')

@app.route('/', methods=['POST','GET'])
def search():
    print "in search"
    name = request.form['cname']
    query = Query()
    #courses = query.getCourseInfoByName(name)
    if request.method == 'POST':
        return render_template('course.html')
        # return redirect(url_for('index'))
    return "what"


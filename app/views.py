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
    courses = query.getCourseInfoByName(name)
    print courses
    if request.method == 'POST':
        return render_template('course.html')
        # return redirect(url_for('index'))
    return "what"

@app.route('/comm', methods=['POST','GET'])
def addCom():
    print "in add com"
    return render_template('comment.html')

@app.route('/update', methods=['POST','GET'])
def update():
    print "in update"
    postId = request.args.get('postId')
    print postId
    return render_template('comment.html')

@app.route('/delete', methods=['POST','GET'])
def delete():
    print "in delete"
    postId = request.args.get('postId')
    print postId
    return redirect(url_for('index'))
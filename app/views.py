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
    cid = courses[0][0]
    reviews = query.getReviewsByCid(cid)
    print reviews
    print courses
    if request.method == 'POST':
        return render_template('course.html', course=courses[0], revs=reviews)
    return "what"


@app.route('/comm', methods=['POST','GET'])
def addCom():
    print "in add com"
    print request.method
    if request.method == 'POST':
        return render_template('landing.html')
    return render_template('comment.html')

@app.route('/update', methods=['POST','GET'])
def update():
    print "in update"
    print request.method
    postId = request.args.get('postId')
    print postId
    return render_template('comment.html')

@app.route('/delete', methods=['POST','GET'])
def delete():
    print "in delete"
    postId = request.args.get('postId')
    print postId
    return redirect(url_for('index'))
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
    try:
        stat = roundVals(query.get_stats(cid)[0])
    except Exception:
        stat = 0
    if request.method == 'POST':
        return render_template('course.html', course=courses[0], revs=reviews, stat=stat)
    return "what"

@app.route('/login', methods=['POST', 'GET'])
def login():
    print "in login"
    if "loggedIn" in session and session['loggedIn'] == "in":
        print "already logged in"
    print "one"
    user = request.form['login-email']
    passw = request.form['login-pass']

    auth = authenticate(user, passw)

    if auth:
        print "send message saying logged in"
    else:
        print "not logged in"

    return render_template('landing.html')

def authenticate(user, passw):
    print "add code to check user and pass"

@app.route('/comm', methods=['POST','GET'])
def addCom():
    print "in add com"
    print request.method
    cid = request.args.get('courseId')
    print cid
    if request.method == 'POST':
        query = Query()
        cid2 = request.form['cid']

        query.ins_review_replWrd("temp@illinois.edu", request.form['toughness'], request.form['work'], request.form['rating'],
                                 request.form['rev'], cid2,"fuck","fudge")

        reviews = query.getReviewsByCid(cid2)
        course = query.getCourseInfoByCid(cid2)
        stat = roundVals(query.get_stats(cid2)[0])
        print stat

        return render_template('course.html', course=course[0], revs=reviews, stat=stat)

    return render_template('comment.html', type='com', cid=cid)

@app.route('/update', methods=['POST','GET'])
def update():
    print "in update"
    query = Query()


    cid = request.args.get('cid')
    rev = []
    if request.method == 'GET':
        postId = request.args.get('postId')
        rev = query.getReviewsByCid(postId)
        print postId
        print rev

    if request.method == 'POST':
        cid2 = request.form['cid']
        postId2 = request.form['revid']


        query.updateRev(postId2, request.form['rev'], request.form['toughness'],
                                 request.form['work'],
                                 request.form['rating'])

        reviews = query.getReviewsByCid(cid2)
        course = query.getCourseInfoByCid(cid2)
        stat = roundVals(query.get_stats(cid2)[0])

        return render_template('course.html', course=course[0], revs=reviews, stat=stat)

    if len(rev) <= 0:
        rev = [""]
    return render_template('comment.html', type='up', cid=cid, rev=rev[0], revid=postId)

@app.route('/delete', methods=['POST','GET'])
def delete():
    print "in delete"
    postId = request.args.get('postId')
    print postId
    query = Query()
    query.deleteReview(postId)
    cid = request.args.get('cid')
    reviews = query.getReviewsByCid(cid)
    courses = query.getCourseInfoByCid(cid)
    stat = roundVals(query.get_stats(cid)[0])

    return render_template('course.html', course=courses[0], revs=reviews, stat=stat)

def roundVals(tup):
    return tuple(round(itup,1) for itup in tup)

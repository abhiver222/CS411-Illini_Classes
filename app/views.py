from app import app
from flask import render_template, request, session, flash, redirect, url_for, jsonify
from app.data.query import Query
from app.data.review_analysis.ReviewSummarizer import *
from app.data.review_analysis.SentimentAnalyser import *

def checkLoggedIn():
    if "loggedIn" in session and session['loggedIn'] == "in":
        return 1
    return 0

@app.route('/')
@app.route('/index')
def index():
    """
    route renders the landing page
    """
    return render_template('landing.html', loggedIn = checkLoggedIn())

@app.route('/', methods=['POST','GET'])
def search():
    print "in search"
    name = request.form['cname']
    query = Query()
    courses = query.getCourseInfoByName(name)
    cid = courses[0][0]
    reviews = query.getReviewsByCid(cid)
    revList = [r[5] for r in reviews]
    if len(revList) == 0:
        revList.append("")
    # print revList
    combinedRev = ReviewSummarizer(revList).getSummarizedText()
    revTags = SentimentAnalyser(revList).senti_pretrained()
    # print revTags

    try:
        stat = roundVals(query.get_stats(cid)[0])
    except Exception:
        stat = 0

    if request.method == 'POST':
        print reviews
        taggedRevs = tagRevs(reviews,revTags)
        return render_template('course.html', course=courses[0], revs=reviews, stat=stat,
                               combRev=combinedRev, taggedRevs=taggedRevs, loggedIn = checkLoggedIn())
    return "what"

def tagRevs(reviews, tags):
    retRev = {}
    retRev["positive"] = []
    retRev["negative"] = []
    retRev["neutral"]  = []
    for i in range(0,len(tags)):
        retRev[tags[i]].append(reviews[i])
    return retRev


@app.route('/ajaxLogin')
def ajaxLogin():
    user = request.args.get('login_email', 0 , type=str)
    passw = request.args.get('login_password', 0, type=str)
    print "Using Ajax Login"
    auth = authenticate(user, passw)
    if auth:
        print "Ajax Login successful"
        session['loggedIn'] = "in"
        return jsonify(result=True)
    print "Ajax Login unsuccessful"
    return jsonify(result=False)

@app.route('/logout')
def logout():
    session['loggedIn'] = None
    return redirect(url_for('index'))


def authenticate(user, passw):
    print "add code to check user and pass"
    print user
    print passw
    q = Query()
    retL= q.check_auth(user,passw)
    print(retL)
    return (len(retL) != 0)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print "in signup"
    user = request.form["signup-email"]

    passw = request.form["signup-password"]

    name = request.form["username"]
    validNewUser = addUser(user, passw, name)

    return render_template('landing.html', loggedIn = checkLoggedIn())

def addUser(user, passw, name):
    print "adding new user"
    q = Query()
    retL = q.checkIfUserExist(user)
    if len(retL) == 0:
        q.ins_new_user(user, passw, name)
    else:
        print "user exists, send a toast message"

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
        reviews = query.getReviewsByCid(cid2)
        revList = [r[5] for r in reviews]
        print revList
        combinedRev = ReviewSummarizer(revList).getSummarizedText()
        revTags = SentimentAnalyser(revList).senti_pretrained()

        return render_template('course.html', course=course[0], revs=reviews, stat=stat, combRev=combinedRev, loggedIn = checkLoggedIn())

    return render_template('comment.html', type='com', cid=cid, loggedIn = checkLoggedIn())

@app.route('/update', methods=['POST','GET'])
def update():
    print "in update"
    query = Query()


    cid = request.args.get('cid')
    rev = []
    if request.method == 'GET':
        postId = request.args.get('cid')
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

        return render_template('course.html', course=course[0], revs=reviews, stat=stat, loggedIn = checkLoggedIn())

    if len(rev) <= 0:
        rev = [""]
    return render_template('comment.html', type='up', cid=cid, rev=rev[0], revid=postId, loggedIn = checkLoggedIn())

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

    return render_template('course.html', course=courses[0], revs=reviews, stat=stat, loggedIn = checkLoggedIn())

def roundVals(tup):
    return tuple(round(itup,1) for itup in tup)

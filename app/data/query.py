import sqlite3

class Query:
    def __init__(self):
        self.conn  = sqlite3.connect("app/data/class.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    # insert rating, post, review

    def ins_instructor_rating(self, instID, rating):

        query = """INSERT INTO InstructorRatings (instructorID, rating)
                     VALUES ({instID}, {rating})""".format(instructorID=instID,rating=rating)
        self.cur.execute(query)

    def ins_post(self,email,text,crn,mod):

        query = """INSERT INTO Posts (UserEmail, Text, CourseCRN, Modified)
                     VALUES (\"{email}\", \"{text}\", crn, \"{mod}\")""".format(email=email,text=text,crn=crn,mod=mod)
        self.cur.execute(query)

    def ins_review(self,UserEmail, Toughness, Workload, Rating, Text, CourseCRN):

        query = """INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseCRN)
                     VALUES (\"{email}\", {tough}, {work}, {rating}, \"{text}\", {crn})""".format(email=UserEmail,tough=Toughness,
                                                                                                work=Workload,rating=Rating,
                                                                                                text=Text,crn=CourseCRN)
        self.cur.execute(query)


    # insert new user
    def ins_new_user(self, email, passw, name):

        query = """INSERT INTO Users (Email, Password, Name)
                    VALUES (\"{email}\", \"{passw}\", \"{name}\")""".format(email=email,passw=passw,name=name)
        self.cur.execute(query)

    # selection queries

    def getCourseInfoByName(self,courseName):

        query = """SELECT * FROM Courses WHERE Name = \"{name}\"""".format(name=courseName)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getCourseInfoByName(self,crn):

        query = """SELECT * FROM Courses WHERE CRN = \"{crn}\"""".format(crn=crn)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getComments(self,crn):
        query = """SELECT * FROM Reviews WHERE CourseCRN = {crn}""".format(crn=crn)
        self.cur.execute(query)
        return self.cur.fetchall()
    # delete Reviews
    def deleteReview(self, reviewID):
        query = """DELETE FROM Reviews where ID = '{rid}'""".format(rid = reviewID)
        self.cur.execute(query)
    # delete Post
    def deletePost(self, postID):
        query = """DELETE FROM Posts where ID = '{pid}'""".format(pid = postID)
        self.cur.execute(query)
    # deleteComment
    def deleteComment(self, commentID):
        query = """DELETE FROM Comments where ID = '{cid}'""".format(cid = commentID)
        self.cur.execute(query)




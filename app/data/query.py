import sqlite3

class Query:
    def __init__(self):
        self.conn  = sqlite3.connect("app/data/class.db", check_same_thread=False) # if local
        #self.conn = sqlite3.connect("class.db", check_same_thread=False) # if server
        self.cur = self.conn.cursor()

    # insert rating, post, review

    def ins_instructor_rating(self, instID, rating):

        query = """INSERT INTO InstructorRatings (instructorID, rating)
                     VALUES ({instID}, {rating})""".format(instructorID=instID,rating=rating)
        self.cur.execute(query)
        self.conn.commit()

    def ins_post(self,email,text,crn,mod):

        query = """INSERT INTO Posts (UserEmail, Text, CourseCRN, Modified)
                     VALUES (\"{email}\", \"{text}\", crn, \"{mod}\")""".format(email=email,text=text,crn=crn,mod=mod)
        self.cur.execute(query)
        self.conn.commit()

    def ins_review(self,UserEmail, Toughness, Workload, Rating, Text, CourseCRN):

        query = """INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseCRN)
                     VALUES (\"{email}\", {tough}, {work}, {rating}, \"{text}\", {crn})""".format(email=UserEmail,tough=Toughness,
                                                                                                work=Workload,rating=Rating,
                                                                                                text=Text,crn=CourseCRN)
        self.cur.execute(query)
        self.conn.commit()

    # insert a new review after filtering out the bad words
    def ins_review_replWrd(self,UserEmail, Toughness, Workload, Rating, Text, CourseID,Forbidden,Replword):
        query = """INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES (\"{email}\", {tough}, {work}, {rating}, REPLACE(\" {text}\", \"{forbidden}\", \"{Replword}\"), {crn})""".format(
            email=UserEmail, tough=Toughness,
            work=Workload, rating=Rating,
            text=Text, crn=CourseID, forbidden=Forbidden,Replword=Replword)
        self.cur.execute(query)
        self.conn.commit()

    # update
    def updateRev(self, revId, text, tough, work, rate):
        query = """UPDATE Reviews SET Toughness = {tough}, Workload = {work}, Rating = {rate},
        Text = REPLACE (\"{text}\", \"{forbidden}\", \"{repl}\") WHERE ID = {revid}""".format(
        tough=tough, work=work, rate=rate, text=text, revid=revId, forbidden="fuck", repl="fudge")

        self.cur.execute(query)
        self.conn.commit()

    def checkIfUserExist(self, user):

        query = """SELECT * FROM Users WHERE Email == \"{user}\"""".format(user=user)
        self.cur.execute(query)
        return self.cur.fetchall()

    # insert new user
    def ins_new_user(self, email, passw, name):

        query = """INSERT INTO Users (Email, Password, Name)
                    VALUES (\"{email}\", \"{passw}\", \"{name}\")""".format(email=email,passw=passw,name=name)
        self.cur.execute(query)
        self.conn.commit()

    # check user
    def check_auth(self, email, passw):
        query = """SELECT * FROM Users WHERE Email = \"{user}\" AND Password = \"{passw}\"""".format(user=email, passw=passw)
        self.cur.execute(query)
        return self.cur.fetchall()

    # selection queries

    def get_stats(self,courseID):
        #obtain the avgworkload, avgToughness, avgWOrkload for the course based on reviews
        query="""SELECT AVG(Toughness) AS AvgToughness, AVG(Workload) AS AvgWorkload, AVG(Rating) AS AvgRating
            FROM Reviews
            WHERE CourseID=\"{courseid}\"
            GROUP BY CourseID""".format(courseid=courseID)
        self.cur.execute(query)
        return self.cur.fetchall()



    # course information queries
    def getCourseInfoByName(self,courseName):

        query = """SELECT * FROM Courses WHERE Name LIKE \"%{name}%\"""".format(name=courseName)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getCourseInfoByCid(self,cid):

        query = """SELECT * FROM Courses WHERE CourseId = {cid}""".format(cid=cid)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getReviewsByCid(self,cid):
        query = """SELECT * FROM Reviews WHERE CourseId = {cid}""".format(cid=cid)
        print query
        self.cur.execute(query)
        return self.cur.fetchall()

    # delete Reviews
    def deleteReview(self, reviewID):
        query = """DELETE FROM Reviews where ID = '{rid}'""".format(rid = reviewID)
        self.cur.execute(query)
        self.conn.commit()

    # delete Post
    def deletePost(self, postID):
        query = """DELETE FROM Posts where ID = '{pid}'""".format(pid = postID)
        self.cur.execute(query)
        self.conn.commit()

    # deleteComment
    def deleteComment(self, commentID):
        query = """DELETE FROM Comments where ID = '{cid}'""".format(cid = commentID)
        self.cur.execute(query)
        self.conn.commit()



    # Queries to setup departments and courses
    def insert_departments(self, dept):

        query = """INSERT INTO Departments (Name)
                        VALUES (\"{dept_name}\")""".format(dept_name=dept)
        print query
        self.cur.execute(query)
        self.conn.commit()

    def insert_courses(self, desc, name, comb_reviews, avg_toughness, avg_rating, avg_workload, dept_id):

        query = """INSERT INTO Courses (Description, Name, CombReviews, AvgToughness, AvgRating, AvgWkload, DeptID)
                        VALUES (\"{desc}\", \"{name}\", \"{comb_reviews}\", {avg_toughness}, {avg_rating}, {avg_workload}, {dept_id})""".format(
                            desc=desc, name=name, comb_reviews=comb_reviews, avg_toughness=avg_toughness, avg_rating=avg_rating,
                            avg_workload=avg_workload, dept_id=dept_id
                        )
        print query
        # self.cur.execute(query)
        # self.conn.commit()

    # Addtional query function for review analysis
    def get_all_cids(self):
        query = """SELECT CourseID, Name FROM Courses"""
        # print query
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_text_reviews_cid(self, cid):
        query = """SELECT Text FROM Reviews WHERE CourseId = {cid}""".format(cid=cid)
        # print query
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_text_reviews_no_cid(self):
        query = """SELECT Text FROM Reviews"""
        # print query
        self.cur.execute(query)
        return self.cur.fetchall()

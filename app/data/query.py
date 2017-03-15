import sqlite3

class Query:
    def __init__(self):
        self.conn  = sqlite3.connect("class.db", check_same_thread=False)
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
                             VALUES (\"{email}\", {tough}, {work}, {rating}, REPLACE(\" {text}\", \"{forbidden}\", \"{replword}\"), {crn})""".format(
            email=UserEmail, tough=Toughness,
            work=Workload, rating=Rating,
            text=Text, crn=CourseID, forbidden=Forbidden,Replword=Replword)
        self.cur.execute(query)
        self.conn.commit()

    # insert new user
    def ins_new_user(self, email, passw, name):

        query = """INSERT INTO Users (Email, Password, Name)
                    VALUES (\"{email}\", \"{passw}\", \"{name}\")""".format(email=email,passw=passw,name=name)
        self.cur.execute(query)
        self.conn.commit()

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

        query = """SELECT * FROM Courses WHERE Name = \"{name}\"""".format(name=courseName)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getCourseInfoByName(self,crn):

        query = """SELECT * FROM Courses WHERE CRN = \"{crn}\"""".format(crn=crn)
        self.cur.execute(query)

        return self.cur.fetchall()

    def getReviews(self,crn):
        query = """SELECT * FROM Reviews WHERE CourseCRN = {crn}""".format(crn=crn)
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

    def insert_courses(self, crn, desc, name, comb_reviews, avg_toughness, avg_rating, avg_workload, dept_id):

        query = """INSERT INTO Courses (CRN, Description, Name, CombReviews, AvgToughness, AvgRating, AvgWkload, DeptID)
                        VALUES ({crn}, \"{desc}\", \"{name}\", \"{comb_reviews}\", {avg_toughness}, {avg_rating}, {avg_workload}, {dept_id})""".format(
                            crn=crn, desc=desc, name=name, comb_reviews=comb_reviews, avg_toughness=avg_toughness, avg_rating=avg_rating,
                            avg_workload=avg_workload, dept_id=dept_id
                        )
        print query
        # self.cur.execute(query)
        # self.conn.commit()

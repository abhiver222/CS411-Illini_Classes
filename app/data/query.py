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
    def ins_new_user
import sqlite3

sqlFile = "class.db"
conn = sqlite3.connect(sqlFile)
cur = conn.cursor()

#print(cur.execute("SELECT * FROM Departments").fetchall())




#cur.execute("""INSERT INTO Courses VALUES ("The course that was inserted for the only purpose of testing","AAS462 IlliniClasses Course",  "Horrible DB design",3.6, 3.9, 4.8,1 )
#""")



'''cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Chapman, W","Spring 2017",5)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Chapman, W ")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",5)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Haberman, M ","Spring 2017",4)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Haberman, M  ")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",2)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Heeren, C","Spring 2017",12)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Heeren, C ")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",3)""")


cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Parameswaran, A","Spring 2017",22)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Parameswaran, A  ")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",5)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Chekuri, C","Spring 2017",18)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Chekuri, C  ")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",2)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Cunningham, R","Spring 2017",10)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Cunningham, R")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",3)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Evans, G","Spring 2017",13)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Evans, G")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",4)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Kloeckner, A","Spring 2017",16)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Kloeckner, A")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",5)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Herman, G","Spring 2017",12)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Herman, G")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",2)""")

cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Gui, H","Spring 2017",23)""") #16 Heeren, C Spring 2017
cur.execute("""INSERT into Instructors(Instructor_Name) VALUES ("Gui, H")""")
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",4)""")'''

#cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
 #                           VALUES ("jane2@illinois.edu", 3.5, 4.5, 3.7, REPLACE("", \"{forbidden}\", \"{replword}\"), {crn})"""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES ("jane2@illinois.edu", 3.5, 4.5, 3.7,"As you've probably heard, this is a legendary course at UIUC. It's one of the most important and well-taught courses here. This course will open many internship opportunities for you, as many interview questions come straight from CS 225. I'd recommend taking this course in the spring semester of your freshman year, so that you will be prepared for the fall recruiting season. The first few weeks of the course will teach you some C++ fundamentals, but that will change soon (CS 126 will do this job instead). You should get comfortable with pointers and dynamic memory. Some MPs are harder than the others. MP3 is pretty hard if you're not comfortable with pointers. MP 5 to 7 are easy to code, but can be hard to understand the concepts at first. Start your MPs early, the queue can get pretty long when deadline gets close.", 11)""")



cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES ("jack32@illinois.edu", 3.2, 5, 5,"This is pretty much the most organised class at UIUC in my opinion. for better or worse the material has stayed pretty much the same over the years", 12)""")

cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES ("adam2@illinois.edu", 3.1, 4, 4.5,"Good Course. But super hectic", 11)""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES ("adam2@illinois.edu", 5, 4, 3.5,"Couldn't manage workload.Dropped after a few weeks", 11)""")


cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)
                             VALUES ("adam2@illinois.edu", 2, 3.4, 3.5,"The best course in UIUC to get intersnshipa", 11)""")

cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)VALUES ("adam2@illinois.edu", 2, 3.4, 3.5,"Good course. Helps in getting internships ", 22)""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)VALUES ("juk90@illinois.edu", 2, 4.4, 3.6,"The professor is good. Works best when taken after taking web prgramming course since it will be useful for creating the projects ", 22)""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)VALUES ("ajk45@illinois.edu", 4, 4, 3.7,"Helpful Course", 22)""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)VALUES ("jane2@illinois.edu", 5, 5, 5,"Interesting course. But had to drop since I couldnt manage CS225 along with it ", 22)""")
cur.execute("""INSERT INTO Reviews (UserEmail, Toughness, Workload, Rating, Text, CourseID)VALUES ("hue2@illinois.edu", 4, 4, 4,"When I took this course, there are 3-4 required MPs, several quizzes, one project and a final. The class is a flipped classroom where students watch online lecture videos at their own pace and then meet once a week to go over concepts. In my opinion, the average workload of this course largely depends on whether or not you've had prior experience in database projects. I'm going to put down 7-10 hours a week because a lot time is required to do the project, especially if you go into the class knowing nothing. Otherwise, this class is a good and useful elective. (Note: find good teammates for your project!) ", 22)""")



#print(cur.execute("SELECT * FROM Courses").fetchall())
#print(cur.execute("SELECT * FROM Instructors").fetchall())
#print(cur.execute("SELECT * FROM Teaches").fetchall())
print(cur.execute("SELECT * FROM Reviews").fetchall())

conn.commit()
conn.close()
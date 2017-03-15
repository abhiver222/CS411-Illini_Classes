import sqlite3

sqlFile = "class.db"
conn = sqlite3.connect(sqlFile)
cur = conn.cursor()

#print(cur.execute("SELECT * FROM Departments").fetchall())




#cur.execute("""INSERT INTO Courses VALUES ("The course that was inserted for the only purpose of testing","AAS462 IlliniClasses Course",  "Horrible DB design",3.6, 3.9, 4.8,1 )
#""")



cur.execute("""iNSERT into Teaches(InstructorName,Semester,CourseID) VALUES ("Chapman, W","Spring 2017",5)""") #16 Heeren, C Spring 2017
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
cur.execute("""INSERT into InstructorRatings(InstructorID,Rating) VALUES ("""+str(cur.lastrowid)+""",4)""")









print(cur.execute("SELECT * FROM Courses").fetchall())
print(cur.execute("SELECT * FROM Instructors").fetchall())
print(cur.execute("SELECT * FROM Teaches").fetchall())

conn.commit()
conn.close()
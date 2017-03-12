import sqlite3

sqlFile = "class.db"
#table1 = "commentsTable"
#table2 = "repliesTable"

conn = sqlite3.connect(sqlFile)
cur = conn.cursor()

cur.execute("""Create table Comments( ID INTEGER PRIMARY KEY AUTOINCREMENT,
	UserEmail  TEXT,
	Text TEXT,
	Modified TEXT)""")

cur.execute("""Create table Posts(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	UserEmail  TEXT,
	Text TEXT,
	CourseCRN INTEGER,
	Modified TEXT
)
""")

cur.execute("""Create table Teaches(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	InstructorName  TEXT,
	Semester TEXT,
	CourseCRN INTEGER

)"""
)

cur.execute("""CREATE TABLE Instructors(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Instructor_Name TEXT

)
""")

cur.execute("""CREATE TABLE Departments(
DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT ,
Name TEXT
)
""")
cur.execute("""CREATE TABLE InstructorRatings(
ID INTEGER PRIMARY KEY AUTOINCREMENT ,
InstructorID INTEGER,
Rating INTEGER
)
""")


cur.execute("""Create table Reviews(
    ID INTEGER PRIMARY KEY AUTOINCREMENT ,
	UserEmail  TEXT,
	Toughness INTEGER,
	Workload INTEGER,
	Rating INTEGER,
	Text varchar(750),
CourseCRN INTEGER
)
""")

cur.execute("""Create table Courses(
    CRN INT PRIMARY KEY  ,
	Description  TEXT,
	Name TEXT,
	CombReviews TEXT,
	AvgToughness numeric,
	AvgRating numeric,
	AvgWkload numeric,

	DeptID INTEGER

)""")


cur.execute("""Create table Users(

	Email TEXT PRIMARY KEY ,
	Password TEXT,
	Name TEXT

)""")





'''cur.execute("""create table {com} (comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   project TEXT,comment_text TEXT)""".format(com=table1))

cur.execute("""create table {rep} (reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   parent_comment_number INTEGER, parent_project TEXT,comment TEXT)""".format(rep=table2))'''


#cur.execute("""create table forbiddenWords (word TEXT, replacement TEXT)""")

'''insert_stmt = """
                         Insert into repliesTable (parent_comment_number, parent_project,
                                                  comment) values ({num}, {par}, {com})
               """.format(num=1, par="\"Assignment0\"", com="\"hello world ?\"")
# print insert_stmt

# insert_stmt = "delete from commentsTable where comment_id = 7"
cur.execute(insert_stmt)
cur.execute("select * from repliesTable")
print cur.fetchall()'''

conn.commit()
conn.close()



import sqlite3

sqlFile = "class.db"
conn = sqlite3.connect(sqlFile)
cur = conn.cursor()

#print(cur.execute("SELECT * FROM Departments").fetchall())




cur.execute("""INSERT INTO Courses VALUES ("The course that was inserted for the only purpose of testing","AAS462 IlliniClasses Course",  "Horrible DB design",3.6, 3.9, 4.8,1 )
""")
cur.execute("""INSERT into Instructors()""")

print(cur.execute("SELECT * FROM Courses").fetchall())
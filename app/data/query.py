import sqlite3

class Query:
    def __init__(self):
        self.conn  = sqlite3.connect("app/data/class.db", check_same_thread=False)
        self.cur = self.conn.cursor()


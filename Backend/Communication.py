import sqlite3
import datetime

from Objects import Person, Job, UserAlreadyExists

### THIS CODE IS FOR LOCAL PURPOSES AND FOR TESTING PURPOSES ONLY ###
### THIS CLASS WILL BE REFACTORED TO SQLALCHEMY IN THE FUTURE ###

class Database:

    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, amount REAL)") # Create table for people to keep track
        self.c.execute("CREATE TABLE IF NOT EXISTS completed (person INTEGER, job TEXT, amount REAL, date TEXT)") # Create table for completed jobs
        self.conn.commit()

    def add_person(self, first_name: str, last_name: str, amount: float = None) -> None:
        self.c.execute("SELECT * FROM people WHERE first = ? AND last = ?", (first_name, last_name))
        if self.c.fetchone():
            raise UserAlreadyExists()
        self.c.execute("INSERT INTO people (first, last, amount) VALUES (?, ?, ?)", (first_name, last_name, amount if amount else 0))
        self.conn.commit()

    def add_job(self, person, job, amount, date: datetime.date) -> None:
        self.c.execute("INSERT INTO completed (person, job, amount, date) VALUES (?, ?, ?, ?)", (person, job, amount, date.isoformat()))
        self.c.execute("SELECT amount FROM people WHERE id = ?", (person,))
        amount = self.c.fetchone()[0] + amount
        self.c.execute("UPDATE people SET amount = ? WHERE id = ?", (amount, person))
        self.conn.commit()

    def get_person(self, first_name, last_name):
        self.c.execute("SELECT * FROM people WHERE first = ? AND last = ?", (first_name, last_name))
        p = Person(*self.c.fetchone())
        self.c.execute("SELECT * FROM completed WHERE person = ?", (p.id,))
        for row in self.c.fetchall():
            p.jobs.append(Job(row))

        return p

import sqlite3

conn = sqlite3.connect('student.sqlite') #connects to the database
cursor = conn.cursor()

#create a student table - SQL COMMAND
create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    id integer PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);
"""

#execute the command
cursor.execute(create_students_table)
conn.close()
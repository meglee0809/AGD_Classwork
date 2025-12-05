import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

select_students = """
SELECT id, firstname, lastname, age
FROM students
WHERE age >= 18
"""

cursor.execute(select_students)

first_person = cursor.fetchone()
more_people = cursor.fetchmany(10)
other_people = cursor.fetchall() # does NOT include the previous people

print(first_person)
print(more_people)
print(other_people)

conn.close()
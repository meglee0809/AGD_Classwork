import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

#update ONE record
update_query = """
UPDATE students
SET lastname = ?
WHERE id = 49;
"""

cursor.execute(update_query, ("???",)) # does this when lastname is Jackie!!
conn.commit()

#update MULTIPLE records
increment_age_query = """
UPDATE students
SET age = age - 1;
"""
cursor.execute(increment_age_query)
conn.commit()
conn.close()


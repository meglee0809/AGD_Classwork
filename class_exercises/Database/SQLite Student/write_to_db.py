import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

parameterised_insert_query = """
INSERT INTO Students (FirstName, LastName, Age, Gender) 
VALUES (?, ?, ?, ?);
"""

fake = Faker('en_GB')
fake.random.seed(42)
random.seed(42)

student_data = []
for _ in range(100):
    gender = random.choice(('Female', 'Male'))
    if gender == 'Male':
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
    age = random.randint(1,30)
    student_data.append((first_name, last_name, age, gender))

cursor.executemany(parameterised_insert_query,student_data)
conn.commit() #DONT FORGET
conn.close()
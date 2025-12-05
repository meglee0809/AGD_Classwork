import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

insert_query = """
INSERT INTO Students (FirstName, LastName, Age, Gender) 
VALUES ('Miho', 'Akemisu', 16, 'Female');
"""

fake = Faker('en_GB')
fake.random.seed(42)

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


cursor.execute(paramterised_insert_query,())
conn.commit() #DONT FORGET
conn.close()
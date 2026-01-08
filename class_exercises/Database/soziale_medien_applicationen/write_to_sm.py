import sqlite3
conn = sqlite3.connect("soziale_medien.db")

users_data = [('James', 25, 'male', 'USA'), ('Leila', 32, 'female', 'France'), ('Brigitte', 35, 'female', 'England'), ('Mike', 40, 'male', 'Denmark'), ('Elizabeth', 21, 'female', 'Canada'),]

cursor = conn.cursor()
parameterised_insert_query = """
INSERT INTO users (Name, Age, Gender, Nationality) 
    VALUES (?, ?, ?, ?);
"""

cursor.executemany(parameterised_insert_query,users_data)
conn.commit() #DONT FORGET
conn.close()
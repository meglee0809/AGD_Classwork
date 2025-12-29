# Connect the database to Python using the sqlite3 module
import sqlite3

# Connect
conn = sqlite3.connect("chinook.sqlite")
# A cursor is a pointer to a place in the database which allows access to a table row-by-row
cursor = conn.cursor()
# This is the SQL query
query = "SELECT FirstName, LastName, Title FROM employees;"
# The cursor executes the query
cursor.execute(query)
# Fetch statements bring sequential rows from the table into python tuples
employee_1 = cursor.fetchone()
employees_2_3 = cursor.fetchmany(2)
employees_rest = cursor.fetchall()

print(employee_1)
print(employees_2_3)
print(employees_rest)

conn.close()

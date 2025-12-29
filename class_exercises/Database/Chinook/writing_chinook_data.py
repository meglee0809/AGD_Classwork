import sqlite3
conn = sqlite3.connect("chinook.sqlite")

# Insert a new genre
cursor = conn.cursor()
query = 'INSERT INTO genres (Name) values ("Funk");'
cursor.execute(query)

#1
customerlist = []
query = 'SELECT FirstName,LastName,Address FROM Customers;'
cursor.execute(query)
customerlist = cursor.fetchall()
print(customerlist)

#2
protectedtrackslist = []
query = 'SELECT * FROM tracks WHERE MediaTypeId = 2;'
cursor.execute(query)
protectedtracks = cursor.fetchall()
print(protectedtracks)

#3

cityes = []
seen = set()
counted_cityes = []

query = 'SELECT City, COUNT(*) AS count FROM customers GROUP BY City ORDER BY count DESC;'
cursor.execute(query)
cityes = cursor.fetchall()
print(cityes)

#4
query = 'INSERT INTO media_types (Name) VALUES ("Windows Media Audio");'
cursor.execute(query)
query = 'INSERT INTO media_types (Name) VALUES ("FLAC audio file");'
cursor.execute(query)

#5
NEreports = []
query = 'SELECT FirstName, LastName FROM employees WHERE ReportsTo = 2;'
cursor.execute(query)
NEreports = cursor.fetchall()
print(NEreports)

# Before a change is written to the database, it must be committed
conn.commit()
conn.close()

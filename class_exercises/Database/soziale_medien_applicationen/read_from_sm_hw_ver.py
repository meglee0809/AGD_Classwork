# Connect the database to Python using the sqlite3 module
import sqlite3

# Create a connection to the database
conn = sqlite3.connect("soziale_medien.db")

# Create a cursor
cursor = conn.cursor()

# Create a SELECTION command
select_posts = """
SELECT title, description
FROM posts
"""

#1.	Retrieve all the comments text which end with a question mark
questionable_posts = """
SELECT text
FROM comments
WHERE text LIKE '%?'
"""

#2.	Change Elizabeth’s name to “Lizzy” in the users table.
lizzy = """
UPDATE users
SET name = 'Lizzy'
WHERE name = 'Elizabeth'
"""

#3.	Show the names of users and the number of posts that they have written.
users_written_posts = """
SELECT users.name as Name, COUNT(posts.user_id) as posts
FROM users,posts
WHERE posts.user_id = users.id
GROUP BY posts.user_id
"""

#4.	Show the names of users and each of the comments that they have written.
users_comments_posts = """
SELECT users.name, comments.text
FROM users INNER JOIN comments ON users.id = comments.user_id
ORDER BY users.id
"""

# Fetch all posts
posts = cursor.execute(users_comments_posts).fetchall()

# Close the connection
conn.close()

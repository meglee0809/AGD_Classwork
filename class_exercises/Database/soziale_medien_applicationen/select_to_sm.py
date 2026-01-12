import sqlite3

#this returns all of the records from the query
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

#---------------------------------------------------------------------
#selecting all the users from the table
select_users = "SELECT * from users"
select_posts = "SELECT * from posts"

with sqlite3.connect("soziale_medien.db") as conn:
    users = execute_read_query(conn, select_users)
    posts = execute_read_query(conn, select_posts)

#for user in users:
    #print(user)
#for post in posts:
    #print(post)

#----------------------------------------------------------------------
#joining stuff - retrieves data from two related tables
select_users_posts = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users ON posts.user_id = users.id 
"""
# INNER JOIN users (the table) ON posts.user_id (

users_posts = execute_read_query(conn, select_users_posts)
#for post in users_posts:
    #print(post)

#joining MULTIPLE stuffs ------------------------------
select_posts_comments_users = """
SELECT
    posts.description as post,
    comments.text as comment,
    users.name
FROM
    posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(
    conn, select_posts_comments_users
)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

#gives the names of the columns --------------------------------------
cursor = conn.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]

print(column_names)

#--------------------------------------------------------------------
#WHERE - returns specific stuff

#the as just renames the columns so that when you acc read it you dont see description you see post
select_post_likes = """
SELECT
    description as Post,
    COUNT(likes.id) as Likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    likes.post_id
"""

post_likes = execute_read_query(conn, select_post_likes)

for post_like in post_likes:
    print(post_like)

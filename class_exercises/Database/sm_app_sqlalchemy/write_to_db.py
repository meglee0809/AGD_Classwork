import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

sqlite_engine = sa.create_engine('sqlite:///social_media.db', echo=True)

# Create a session
session = so.Session(bind=sqlite_engine)

# Create examples of Users
users = [User(name="Alice", age=30, gender="Female", nationality="Canadian"),
         User(name="Bob", age=25, gender="Male", nationality="American"),
         User(name="Charlie", age=28, gender="Male", nationality="British"),
         User(name="Diana", age=22, gender="Female", nationality="Australian"),
         ]

session.add_all(users)
session.commit()
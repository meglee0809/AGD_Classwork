from sqlalchemy import create_engine
from create_db import Base

engine = create_engine('sqlite:///activities.sqlite', echo=True)

# drop any existing tables.
Base.metadata.drop_all(engine)

# create new tables according to the tables in Base
Base.metadata.create_all(engine)


class Person:
    pass
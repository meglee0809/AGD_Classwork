from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from model import Person

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)
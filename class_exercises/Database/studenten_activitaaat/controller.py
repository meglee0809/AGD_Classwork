import sqlalchemy as sa
import sqlalchemy.orm as so

from model import Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_activities_people(self,activities_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activities_name)
            activity = session.scalar(stmt)
            peoples = activity.attendees #the name mr dales chose !!
            people_names = [{person.first_name, person.last_name} for person in peoples]
        return people_names

    def add_person(self,first_name,last_name):
        with so.Session(bind=self.engine) as session:
            person = Person(first_name=first_name, last_name=last_name)
            session.add(person)
            session.commit()

    def delete_person(self, person_id):
        with so.Session(bind=self.engine) as session:
            person = session.get(Person, person_id)
            session.delete(person)
            session.commit()


    def edit_person(self, person_id, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            person = session.get(Person, person_id)
            person.first_name = first_name
            person.last_name = last_name
            session.commit()


    def add_activity(self,activity_name):
        with so.Session(bind=self.engine) as session:
            activity = Activity(name=activity_name)
            session.add(activity)
            session.commit()

    def delete_activity(self, activity_id):
        with so.Session(bind=self.engine) as session:
            activity = session.get(Activity, activity_id)
            session.delete(activity)
            session.commit()

    def edit_activity(self, activity_id, activity_name):
        with so.Session(bind=self.engine) as session:
            activity = session.get(Activity, activity_id)
            activity.name = activity_name
            session.commit()

if __name__ == '__main__':
    controller = Controller()

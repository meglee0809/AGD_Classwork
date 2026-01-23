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

    def get_activities_peopl(self,activities_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activities_name)
            activity = session.scalar(stmt)
            peoples = activity.person
            people_names = [{person.firstname, person.last_name} for person in peoples]


    def edit_person(self):
        pass

    def add_person(self):
        pass

    def delete_person(self):
        pass

    def edit_activity(self):
        pass

    def add_activity(self):
        pass

    def delete_activity(self):
        pass

if __name__ == '__main__':
    controller = Controller()

#import pyinputplus as pyip
from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)

    def show_activities_people(self):
        activity_name = input('Enter activity names: ')
        peoples = self.controller.get_activities_people(activity_name)
        for people in peoples:
            print(people)

    def add_person(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        person = self.controller.add_person(first_name, last_name)

    def delete_person(self):
        person_id = input('Enter person ID: ')
        person = self.controller.delete_person(person_id)

    def add_activity(self):
        activity_name = input('Enter activity names: ')
        activity = self.controller.add_activity(activity_name)

    def delete_activity(self):
        activity_id = input('Enter activity ID: ')
        activity = self.controller.delete_activity(activity_id)

    def edit_person(self):
        person_id = input('Enter person ID: ')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        person = self.controller.edit_person(person_id, first_name, last_name)

    def edit_activity(self):
        activity_id = input('Enter activity ID: ')
        activity_name = input('Enter activity names: ')
        activity = self.controller.edit_activity(activity_id, activity_name)

if __name__ == '__main__':
    cli = CLI()


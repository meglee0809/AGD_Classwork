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

    def edit_person(self):


    def add_person(self):


    def delete_person(self):


    def edit_activity(self):


    def add_activity(self):


    def delete_activity(self):


if __name__ == '__main__':
    cli = CLI()

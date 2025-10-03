#dog class exercises

class Dog:
    def __init__(self,name,age): #__init__ is
        self.name = name #self refers to the Dog itself
        self.age = age

    def speaks(self): #if dogname.speaks() is used it will return the below
        return f'{self.name} says woof woof'


grey = Dog('Grey',4)
#dog class exercises
class Dog:
    species = "Canis familiaris" #same for all 'dogs'
    def __init__(self, name, age): #declaring attributes of the class
        self.name = name
        self.age = age
    def speak(self,sound):
        return f"{self.name} says {sound}!"
    def __str__(self): #this gives the attributes of that specific dog
        return f"{self.name} is {self.age} years old :)"

grey = Dog("Grey",4)
pumi = Dog("Pumi",5)

#tests
print(grey.name)
print(grey.age)
print(grey.speak("woof")) #to use def functions you need the dog.function(stuff)
print(grey) #def __str__ test
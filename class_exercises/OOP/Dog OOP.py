#dog class exercises
class Dog: #superclass
    species = "Canis familiaris" #class attribute : same for all 'dogs'
    def __init__(self, name, age): #declaring attributes of the class
        self.name = name
        self.age = age
    def speak(self,sound):
        return f"{self.name} barks {sound}!"
    def __str__(self): #this gives the attributes of that specific dog
        return f"{self.name} is {self.age} years old :)"

class Dachshund(Dog): #(dog) means its a type of dog but unique to others dogs
    def speak(self, sound = "GUINESS"): #this is a modifier for dachshund of the original speak
        return super().speak(sound) # super makes it so that you run the original speak


grey = Dog("Grey",4)
pumi = Dog("Pumi",5)
potato = Dachshund("Potato",6)
potato.name = "potato the magnificent" #how to change an attribute
#tests
print(grey.name)
print(grey.age)
print(grey.speak("woof")) #to use def functions you need the dog.function(stuff)
print(grey) #def __str__ test
print(potato.speak())
print(potato)
print(isinstance(potato,Dachshund)) #potato is both, grey is only a dog
print(isinstance(potato,Dog))
print(isinstance(grey,Dachshund))
print(potato.__dict__) #puts potato's attributes into a dictionary


class Car:
    def __init__(self,colour,mileage):
        self.colour = colour
        self.mileage = mileage
    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles"

taycan = Car("blue",20000)
mini = Car("red", 30000)

print(taycan)
print(mini)
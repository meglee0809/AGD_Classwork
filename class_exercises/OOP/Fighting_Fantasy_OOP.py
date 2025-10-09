import random

def dice_sum(num_dice: int = 1,num_sides: int = 6):
    """ use this to sum the rolls instead of for i in range """ #the info in the triple " is given about the function  with help(function)
    '''i'm better'''
    total = sum(random.randint(1,num_sides) for i in range(num_dice))
    return total


class Character:
    def __init__(self,name,skill,stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina}"

    def find_score(self):
        self.roll = dice_sum(2)
        self.score += self.roll


dragon = Character("Rawry the dragon",10,22)

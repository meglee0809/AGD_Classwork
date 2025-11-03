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

    def __repr__(self): #this is dunder keys
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina}"

    def find_score(self):
        self.roll = dice_sum(2)
        self.score = self.roll + self.skill

    def take_hit(self, damage=2):
        self.stamina -= damage

    def fight_round(self,op):
        self.find_score()
        op.find_score()
        #you win
        if self.score > op.score:
            op.take_hit()
            print(f"{op.name} takes a hit!!")
        #op wins
        elif self.score < op.score:
            self.take_hit()
            print(f"{self.name} got hit!!")

        else:
            self.take_hit(1)
            op.take_hit(1)
            print(f"You both got hit!!")

    def return_char_status(self):
        return(f"{self.name} has {self.stamina} stamina !")

    def return_rolls_status(self):
        return(f"{self.name} rolled a {self.roll} with a total score of {self.score} !")

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter #this decorator modifies what the function does -> if you do orc.is_dead = True, it kills him lol
    def is_dead(self, dead: bool):                                    #if you do orc.is_dead = False, it revives him with 1 stamina
        if dead:
            self.stamina = 0
        else:
            self.stamina = min(self.stamina, 1)


class PlayerCharacter(Character):
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina) #uses the super class init function
        self.luck = luck

    @classmethod
    def generate_player_character(cls, name):
        skill = 6 + dice_sum(1)
        stamina = 12 + dice_sum(2)
        luck = 6 + dice_sum(1)
        return cls(name,skill,stamina,luck)

kris = Character("Kris",11,13)
dragon = Character("Rawry the dragon",10,22)
flavia = PlayerCharacter.generate_player_character("Flavia")
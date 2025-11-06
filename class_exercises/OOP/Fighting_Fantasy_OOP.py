
import random

def dice_sum(num_dice: int = 1,num_sides: int = 6):
    """ use this to sum the rolls instead of for i in range """ #the info in the triple " is given about the function  with help(function)
    '''i'm better'''
    total = sum(random.randint(1,num_sides) for i in range(num_dice))
    return total


class Character:
    def __init__(self,name,skill,stamina):
        self.name = name.title()
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self): #this is a dunder key that produces 'computer' readable content
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def __str__(self): #this is another dunder key that should produce HUMAN readable content
        return f'{self.name}'

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
            print(f"-- {op.stamina} damage --")
            result = "won"
            return result

        #op wins
        elif self.score < op.score:
            self.take_hit()
            print(f"{self.name} got hit!!")
            print(f"-- {self.stamina} damage --")
            result = "lost"
            return result

        #draw
        else:
            self.take_hit(1)
            op.take_hit(1)
            print(f"You both got hit!!")
            result = "draw"
            return result

    def return_character_status(self):
        return(f"{self.name} has skill {self.skill} and stamina {self.stamina} !")

    def return_roll_status(self):
        return(f"{self.name} rolled a {self.roll} for a total score of {self.score} !")

    @property
    def is_dead(self):
        return self.stamina <= 0 #returns boolean

    @is_dead.setter #this decorator modifies what the function does -> if you do orc.is_dead = True, it kills him lol
    def is_dead(self, dead: bool):                                    #if you do orc.is_dead = False, it revives him with 1 stamina
        if dead:
            self.stamina = 0
        elif not dead and self.is_dead == True:
            self.stamina = 1



class PlayerCharacter(Character):
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina) #uses the super class init function to inherit ALL ATTRIBUTES including score and roll!!, those are just stated to be used/
        self.luck = luck

    @classmethod #modify a class state that would apply across all the instances of the class NOT a single character
    def generate_player_character(cls, name):
        skill = 6 + dice_sum(1)
        stamina = 12 + dice_sum(2)
        luck = 6 + dice_sum(1)
        return cls(name,skill,stamina,luck)

    def __repr__(self): #this is dunder keys
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    def test_luck(self):
        luck_roll = dice_sum(2)
        self.roll = luck_roll #works cuz player characters have character attributes ASWELL
        if luck_roll <= self.luck:
            self.luck -= 1
            return True
        else:
            self.luck -= 1
            return False


#characters-------------------------------------------------------------------------
elizabeth = PlayerCharacter.generate_player_character("Elizabeth")

kris = Character("Kris",11,13)
dragon = Character("Rawry the dragon",10,22)


#game----------------------------------------------------------------------------------
class Game:
    """Game class - controls the Fighting Fantasy game class"""
    @classmethod
    def load_creatures(cls):
        creatures = [Character("Rawry the dragon",10,10),
                     Character("Jelly-fish",5,5),
                     Character("JELLYF ISH?",10,20),
                     Character("Mildly Warm",8,5),
                     Character("Sluuudge", 2, 10),
                     ]
        return creatures

    def __init__(self):
        self.op = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.op = random.choice(self.creatures)
        self.creatures.remove(self.op)

    def set_player(self,player_character): #use generate_player_character here
        self.player = player_character

    def return_character_statuses(self):
        msg = (self.player.return_character_status() + "\n" +
               self.opponent.return_character_status())
        return msg

    def resolve_fight_round(self): #fights and records the results of the round
        self.round_result = self.player.fight_round(self.op)

    def return_round_results(self):
        msg = (self.player.return_roll_status() + "\n" +
               self.op.return_roll_status() + "\n")
        if self.round_result == "won":
            msg += "You won this round!\n"
        elif self.round_result == "lost":
            msg += "You lost this round.\n"
        else:
            msg += "This round is a draw..\n"
        print(msg)



game = Game()
game.choose_opponent()
game.set_player(elizabeth)
print(game.creatures[2])

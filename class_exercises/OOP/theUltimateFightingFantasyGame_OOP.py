import time
from colorama import Fore,Back,Style
import random


def cooltype(text='Rian',interval=0.03,nextline = True):
    for item in text:
        print(item,end='',flush=True)
        time.sleep(interval)
    if nextline:
        print('\n')

def cooltypecolour(text='Rian',interval=0.05,colour=Fore.MAGENTA,nextline = True):
    print(colour)
    cooltype(text,0.05)
    print(Style.RESET_ALL)
    if nextline:
        print('\n')
def coolinput(text='',interval=0.01):
    for item in text:
        print(item,end='')
        time.sleep(interval)
    return input()

#------------------------------------------

def dice_sum(num_dice: int = 1,num_sides: int = 6):
    """ use this to sum the rolls instead of for i in range """ #the info in the triple " is given about the function  with help(function)
    '''i'm better'''
    total = sum(random.randint(1,num_sides) for _ in range(num_dice))
    return total


class Character:
    def __init__(self,name,skill,stamina):
        self.name = name.title()
        self.skill = skill
        self.stamina = stamina
        self.original_stamina = self.stamina
        self.roll = None
        self.score = None

    def __repr__(self): #this is a dunder key that produces 'computer' readable content
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def __str__(self): #this is another dunder key that should produce HUMAN readable content
        return f'{self.name}'

    def find_score(self):
        self.roll = dice_sum(2)
        self.score = self.roll + self.skill

    def take_hit(self,specificHit=dice_sum(1,8)):
        self.stamina -= specificHit

    def fight_round(self,op):
        self.find_score()
        op.find_score()
        #you win
        if self.score > op.score:
            op.take_hit()
            print(f"{op.name} takes a hit!!")
            print(f"-- {op.name} has {op.stamina} stamina left --")
            result = "won"
            return result

        #op wins
        elif self.score < op.score:
            self.take_hit()
            print(f"{self.name} got hit!!")
            print(f"-- {self.name} has {self.stamina} stamina left --")
            result = "lost"
            return result

        #draw
        else:
            self.take_hit()
            op.take_hit()
            print(f"You both got hit!!")
            result = "draw"
            return result

    def return_character_status(self):
        return f"{self.name} has skill {self.skill} and stamina {self.stamina} !"

    def return_roll_status(self):
        return f"{self.name} rolled a {self.roll} for a total score of {self.score} !"

    @property
    def is_dead(self):
        return self.stamina <= 0 #returns boolean

    @is_dead.setter #this decorator modifies what the function does -> if you do orc.is_dead = True, it kills him lol
    def is_dead(self, dead: bool):                                    #if you do orc.is_dead = False, it revives him with 1 stamina
        if dead:
            self.stamina = 0
        elif self.is_dead:
            self.stamina = 20



class PlayerCharacter(Character):
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina) #uses the super class init function to inherit ALL ATTRIBUTES including score and roll!!, those are just stated to be used/
        self.luck = luck

    @classmethod #modify a class state that would apply across all the instances of the class NOT a single character
    def generate_player_character(cls, name):
        skill = dice_sum(1) #note - used to have a +6
        stamina = dice_sum(5)
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
'''
elizabeth = PlayerCharacter.generate_player_character("Elizabeth")

kris = Character("Kris",11,13)
dragon = Character("Rawry the dragon",10,22)
'''

#game----------------------------------------------------------------------------------
class Game:
    """Game class - controls the Fighting Fantasy game class"""
    @classmethod
    def load_creatures(cls):
        creatures = [Character("Jelly-Fish",2,15),
                     Character("Rawry the dragon",5,25),
                     Character("Mildly Warm",3,10),
                     Character("Sluuudge", 1, 20),
                     ]
        return creatures

    def __init__(self):
        self.op = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.op = random.choice(self.creatures)

    def set_player(self,player_character): #use generate_player_character here
        self.player = player_character

    def return_character_statuses(self):
        msg = (self.player.return_character_status() + "\n" +
               self.op.return_character_status())
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

#--------------------------------------------

class GameCLI:
    """Initialises a game class and launches the script to run the game."""
    def __init__(self):
        self.game = Game()
        self.run_game()

#1) running game------------
    def run_game(self):
        """Welcomes the player to Fighting Fantasy - asks for a player_name
        calls self.game methods to set the player and displays their stats,
        then runs self.fight_opponent"""
        cooltype("You wake up after a long, aimless fall, to ground and no hole.\n"
              "* you hear a fish aimlessly flopping on the ground *")
        cooltype(". . .",0.1)
        cooltype(" I see you have come from above into our grounds.\n"
              "..Welcome to fighting fantasy..")
        cooltype("(the limited limined limined liminal edition)",0.1)

        player_name = input("Enter y o u r name: ")
        self.game.set_player(PlayerCharacter.generate_player_character(player_name))
        self.game.originalStamina = self.game.player.stamina

        cooltype(f"{" ".join(player_name)}... i've never encountered that human name before.."
                 "Welcome. with all my heart. or jelly.. (i suppose)")
        cooltype(self.game.player.return_character_status())
        cooltype("Good luck.")
        time.sleep(2)

        #fight + fight again mechanics
        validFight = True
        while validFight == True:
            self.fight_opponent()
            validuserFight = input("Do you want to fight again? (y/n): ")
            if validuserFight.upper() == "Y":
                validFight = True
                keepStats = input("Do you want to keep your stats? (y/n): ")
                if keepStats.upper() == "N":
                    self.game.set_player(PlayerCharacter.generate_player_character(player_name))
                    self.fight_opponent()
                if keepStats.upper() == "Y":
                    self.game.player.is_dead = False
                    self.fight_opponent()


# boss battle antics--------------------------------------------------------
    def fight_boss_battle(self):
        """you fight the boss lol"""
        print("\n" * 10)
        cooltype("* fish flop.sfx plays *\n"
              "* continued fish flopping noises *\n"
              "The fish jumps flopping onto the ceiling with a burst of jelly "
              "splattering all over the ceiling and the floors.\n"
              "You stare at the red jelly on the ceiling and decide "
              "to leave it instead of eating it.")
        cooltype(". . .",0.1)
        cooltype("long ribbons of tentacles spurt from the blob..\n"
              "the blob slowly floats down..\n"
              "the Jelly-fish has seemingly transformed into JELLYF ISH?\n"
              "..and it's ready for round two.")
        time.sleep(2)
        self.game.op = Character("JELLYF ISH?",6,40)

        valid_fight = True
        while valid_fight == True:
            print("\n" * 5)
            user_ask_fight = input("Do you wish to fight? (Y/N): \n")
            if user_ask_fight.upper() == "Y":
                self.game.resolve_fight_round()
                print(self.game.return_round_results())
                time.sleep(5)
                if self.game.player.is_dead and self.game.op.is_dead:
                    print("\n" * 10)
                    cooltype(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          f"but.. neither did {self.game.op.name}\n"
                          "I suppose not anyone gets a happy ending..\n"
                          "..Leaves a sour taste in your mouth doesn't it?")
                    time.sleep(2)
                    valid_fight = False
                elif self.game.player.is_dead:
                    print("\n" * 10)
                    cooltype("You... {" ".join(player_name)} y o u didn't make it. \n"
                          "..not in the last world and not in t h i s one. \n"
                          "You detect a slight sourness in the fi?s?h'?s tone.\n"
                          "w i l l  y o u  t ry  a g a i n  i n  t h e  n e x t ?")
                    time.sleep(2)
                    valid_fight = False
                elif self.game.op.is_dead:
                    print("\n" * 10)
                    cooltype("You come out v i c t o r i o u s.\n"
                          "The jelly starts to melt into the cracks on the ground..\n"
                          ". . .\n"
                          "The jelly speaks.\n"
                          "How does it feel... victory?\n"
                          "..is it sweet..?\n"
                          "..my jelly forever remains bitter..\n"
                          "The jelly leaves only a sticky red residue to remember it by.\n"
                          "The smell is sour to your nose.\n"
                          f"Y o u, {" ".join(self.game.player.name)}, you have defeated the "
                          f"{self.game.op.name}")
                    time.sleep(5)
                    valid_fight = False

            else:
                print("\n" * 10)
                cooltype("It appears you weren't ready for this..\n"
                      "To flee at the first chance you get.\n")
                cooltype("* fish flop.sfx plays *")
                time.sleep(2)
                valid_fight = False


# 2) fight initiated--------------------------------------------------------
    def fight_opponent(self):
        """Chooses an opponent and displays their stats, then runs self.fight_battle"""
        print("\n" * 10)
        cooltype("An opponent approaches you...")
        self.game.choose_opponent()
        cooltype(f"It appears to be {self.game.op}")
        cooltype({self.game.op.return_character_status()})
        time.sleep(2)
        self.fight_battle()


    def fight_battle(self,):
        """Continues to fight rounds until the player chooses to quit or
        either player or opponent are dead."""
        print("\n" * 10)

        valid_fight = True
        while valid_fight == True:
            print("\n" * 5)
            cooltype(f"{self.game.return_character_statuses()}")
            user_ask_fight = input("Do you wish to fight? (Y/N): \n")
            if user_ask_fight.upper() == "Y":
                self.game.resolve_fight_round()
                print(self.game.return_round_results())
                time.sleep(5)
                if self.game.player.is_dead and self.game.op.is_dead:
                    print("\n" * 10)
                    cooltype(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          f"but.. neither did {self.game.op.name}\n"
                          "I suppose not anyone gets a happy ending..\n"
                          "..Leaves a sour taste in your mouth doesn't it?")
                    time.sleep(2)
                    valid_fight = False
                elif self.game.player.is_dead:
                    print("\n" * 10)
                    cooltype(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          "..not in the last world and not in t h i s one. \n"
                          "will you to try again in the next?")
                    time.sleep(2)
                    valid_fight = False
                elif self.game.op.is_dead:
                    print("\n" * 10)
                    if self.game.op.name == "Jelly-Fish":
                        cooltype("You come out v i c t o r i o u s. /A.e ]?\n"
                              f"You defeated the {self.game.op.name}\n")
                        cooltype(". . . o r  p e r h a p s  n o t  y e t . . .",0.1)
                        time.sleep(2)
                        self.fight_boss_battle()
                    else:
                        cooltype("You come out v i c t o r i o u s.\n"
                              f"You defeated the {self.game.op.name}\n"
                              f"Congratulations {self.game.player.name}!!")
                        time.sleep(2)
                    valid_fight = False

            else:
                print("\n" * 10)
                cooltype("It appears you weren't ready for this..\n"
                      "To flee at the first chance you get.")
                cooltype("* fish flop.sfx plays *")
                time.sleep(2)
                valid_fight = False


if __name__ == "__main__":
    GameCLI()
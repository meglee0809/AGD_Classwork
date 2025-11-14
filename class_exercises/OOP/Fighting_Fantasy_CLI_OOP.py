from Fighting_Fantasy_OOP import Game,Character,PlayerCharacter
from class_exercises.CoolType import cooltype
import time

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
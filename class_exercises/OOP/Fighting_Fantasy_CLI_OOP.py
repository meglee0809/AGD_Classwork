#20:50 -  -5 mins
from Fighting_Fantasy_OOP import Game,Character,PlayerCharacter
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
        print("You wake up after a long, aimless fall, to ground and no hole.\n"
              "* you hear a fish aimlessly flopping on the ground *\n"
              ". . .\n"
              " I see you have come from above into our grounds.\n"
              "..Welcome to fighting fantasy..")
        print("(the limited limined limined liminal edition)")

        player_name = input("Enter y o u r name: ")
        self.game.set_player(PlayerCharacter.generate_player_character(player_name))

        print(f"{" ".join(player_name)}... i've never encountered that human name before..")
        print("Welcome. with all my heart. or jelly.. (i suppose)")
        print(self.game.player.return_character_status())
        print("Good luck.")
        self.fight_opponent()

# boss battle antics--------------------------------------------------------
    def fight_boss_battle(self):
        """you fight the boss lol"""
        print("\n" * 10)
        print("* fish flop.sfx plays *\n"
              "* continued fish flopping noises *\n"
              "The fish jumps flopping onto the ceiling with a burst of jelly "
              "splattering all over the ceiling and the floors.\n"
              "You stare at the red jelly on the ceiling and decide "
              "to leave it instead of eating it.\n")
        print(". . .")
        print("long ribbons of tentacles spurt from the blob..\n"
              "the blob slowly floats down..\n"
              "the Jelly-fish has seemingly transformed into JELLYF ISH?\n"
              "..and it's ready for round two.")

        self.game.op = Character("JELLYF ISH?",6,40)

        valid_fight = True
        while valid_fight == True:
            print("\n" * 5)
            user_ask_fight = input("Do you wish to fight? (Y/N): ")
            if user_ask_fight.upper() == "Y":
                self.game.resolve_fight_round()
                print(self.game.return_round_results())
                if self.game.player.is_dead and self.game.op.is_dead:
                    print("\n" * 10)
                    print(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          f"but.. neither did {self.game.op.name}\n"
                          "I suppose not anyone gets a happy ending..\n"
                          "..Leaves a sour taste in your mouth doesn't it?")
                    valid_fight = False
                elif self.game.player.is_dead:
                    print("\n" * 10)
                    print("You... {" ".join(player_name)} y o u didn't make it. \n"
                          "..not in the last world and not in t h i s one. \n"
                          "You detect a slight sourness in the fi?s?h'?s tone.\n"
                          "w i l l  y o u  t ry  a g a i n  i n  t h e  n e x t ?")
                    valid_fight = False
                elif self.game.op.is_dead:
                    print("\n" * 10)
                    print("You come out v i c t o r i o u s.\n"
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
                    valid_fight = False

            else:
                print("\n" * 10)
                print("It appears you weren't ready for this..\n"
                      "To flee at the first chance you get.\n")
                print("* fish flop.sfx plays *")
                valid_fight = False


# 2) fight initiated--------------------------------------------------------
    def fight_opponent(self):
        """Chooses an opponent and displays their stats, then runs self.fight_battle"""
        print("\n" * 10)
        print("An opponent approaches you...")
        self.game.choose_opponent()
        print(f"It appears to be {self.game.op}")
        print(f"It has {self.game.op.return_character_status()}")
        self.fight_battle()


    def fight_battle(self,):
        """Continues to fight rounds until the player chooses to quit or
        either player or opponent are dead."""
        print("\n" * 10)

        valid_fight = True
        while valid_fight == True:
            print("\n" * 5)
            print(f"{self.game.return_character_statuses()} \n")
            user_ask_fight = input("Do you wish to fight? (Y/N): ")
            if user_ask_fight.upper() == "Y":
                self.game.resolve_fight_round()
                print(self.game.return_round_results())
                if self.game.player.is_dead and self.game.op.is_dead:
                    print("\n" * 10)
                    print(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          f"but.. neither did {self.game.op.name}\n"
                          "I suppose not anyone gets a happy ending..\n"
                          "..Leaves a sour taste in your mouth doesn't it?")
                    valid_fight = False
                elif self.game.player.is_dead:
                    print("\n" * 10)
                    print(f"You... {" ".join(self.game.player.name)}.. y o u didn't make it. \n"
                          "..not in the last world and not in t h i s one. \n"
                          "will you to try again in the next?")
                    valid_fight = False
                elif self.game.op.is_dead:
                    print("\n" * 10)
                    if self.game.op.name == "Jelly-Fish":
                        print("You come out v i c t o r i o u s. /A.e ]?\n"
                              f"You defeated the {self.game.op.name}\n")
                        print(". . . o r  p e r h a p s  n o t  y e t . . .")
                        self.fight_boss_battle()
                    else:
                        print("You come out v i c t o r i o u s.\n"
                              f"You defeated the {self.game.op.name}\n"
                              f"Congratulations {self.game.player.name}!!")
                    valid_fight = False

            else:
                print("\n" * 10)
                print("It appears you weren't ready for this..\n"
                      "To flee at the first chance you get.")
                print("* fish flop.sfx plays *")
                valid_fight = False


if __name__ == "__main__":
    GameCLI()
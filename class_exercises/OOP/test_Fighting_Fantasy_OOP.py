#20:48-21:42
'''
HW NOTES FOR DISCUSSION:
random.seed() -> it ALWAYS uses a specfic number based on the seed value as the first random number
What features do you like about the simulator?
- I like that you roll for luck and fight, but it would be better if you rolled it
before the fighting actually occured
the fact it shows you each roll is nice
What would you do to add to or improve the simulator?
- The game is really easily unbalanced as even an attack difference or 3 and 5,
i rolled around 8 times and the hero never won
- It would also make more sense for the luck to
 also rolled with a dice for damage instead of preset -1 and +1
- with luck it would make more sense to roll one dice to its highest number as equal or under makes no sense
  or you could make it so that luck allows you to roll again (dnd)
- It would be interesting to have different numbers of dice depending on the enemy
'''

import pytest
import random
from .Fighting_Fantasy_OOP import Character, PlayerCharacter


class TestCharacter:
    @pytest.fixture
    def characters(self): #whenever characters are used orc and dragon characters are returned as a preset
        random.seed(10_001) #ALWAYS uses a specfic number based on the seed value as the first random number
        return [Character('orc', skill=5, stamina=12),
                Character('dragon', skill=8, stamina=15)]

    def test_characters(self, characters):
        orc, dragon = characters
        # Test that the orc and dragon character have been set up correctly
        assert orc.name == 'Orc'
        assert orc.skill == 5
        assert orc.stamina == 12
        assert orc.__repr__() == "Character('Orc', skill=5, stamina=12)"
        assert dragon.__str__() == "Dragon"

    def test_find_score(self, characters):
        orc = characters[0]
        orc.find_score()
        assert orc.roll == 4
        assert orc.score == orc.roll + orc.skill

    def test_take_hit(self, characters):
        orc = characters[0]
        orc.take_hit()
        assert orc.stamina == 10
        orc.take_hit(1)
        assert orc.stamina == 9

    def test_fight_round(self, characters):
        orc, dragon = characters
        result = orc.fight_round(dragon)
        assert orc.roll == 4
        assert dragon.roll == 5
        assert dragon.score == 13
        assert result == 'lost'
        assert orc.stamina == 10
        assert dragon.stamina == 15

    def test_is_dead(self, characters):
        orc = characters[0]
        orc.take_hit(12)
        assert orc.is_dead

    def test_set_is_dead(self, characters): #I had to adjust the logic we copied from the board is that okay?
        orc = characters[0]
        orc.is_dead = False
        assert orc.stamina == 12
        orc.is_dead = True
        assert orc.stamina == 0
        orc.is_dead = False
        assert orc.stamina == 1

    def test_return_character_status(self, characters):
        orc = characters[0]
        assert orc.return_character_status() == 'Orc has skill 5 and stamina 12 !'

    def test_return_roll_status(self, characters):
        dragon = characters[1]
        dragon.find_score()
        assert dragon.return_roll_status() == 'Dragon rolled a 4 for a total score of 12 !'


class TestPlayerCharacter:
    @pytest.fixture
    def player_character(self):
        random.seed(10_001)
        return PlayerCharacter.generate_player_character("Sir Tom")

    def test_generate_pc(self, player_character):
        pc = player_character
        assert pc.skill == 9
        assert pc.stamina == 14
        assert pc.luck == 10
        assert pc.__repr__() == "PlayerCharacter('Sir Tom', skill=9, stamina=14, luck=10)"

    def test_test_luck(self, player_character):
        for _ in range(5):
            lucky = player_character.test_luck()
            assert lucky == True
        lucky = player_character.test_luck()
        assert lucky == False
        assert player_character.luck == 4
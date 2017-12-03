import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from rps import RockPaperScissorsGame

new_rps_game = RockPaperScissorsGame()

def test_initial_game_status():
    assert(new_rps_game.player_name == '')

def test_set_player_name():
    new_rps_game.set_player_name('Player')
    assert(new_rps_game.player_name == 'Player')

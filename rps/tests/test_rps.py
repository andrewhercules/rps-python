import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from rps import RockPaperScissorsGame

new_rps_game = RockPaperScissorsGame()

def test_initial_game_status():
    assert(new_rps_game.player_name == '')

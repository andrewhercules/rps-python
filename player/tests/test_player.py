import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from player import Player

new_player = Player()

def test_initial_player_object_status():
    assert(new_player.name == '')

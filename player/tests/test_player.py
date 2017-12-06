import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from player import Player

new_player = Player()

def test_initial_player_object_status():
    assert(new_player.name == '')

def test_set_player_name():
    new_player.set_name('Andrew')
    assert(new_player.name == 'Andrew')

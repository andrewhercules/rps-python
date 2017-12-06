import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from player import Player

def test_initial_player_object_status():
    new_player = Player()
    assert(new_player.name == '')

def test_set_player_name():
    new_player = Player()
    new_player.set_name('Andrew')
    assert(new_player.name == 'Andrew')

def test_set_choice_rock():
    new_player = Player()
    new_player.set_choice('rock')
    assert(new_player.choice == 'rock')

def test_set_choice_paper():
    new_player = Player()
    new_player.set_choice('paper')
    assert(new_player.choice == 'paper')

def test_set_choice_scissors():
    new_player = Player()
    new_player.set_choice('scissors')
    assert(new_player.choice == 'scissors')

def test_set_choice_unknown_choice():
    new_player = Player()
    assert(new_player.set_choice('coffee') == 'Error!')
    assert(new_player.choice == '')

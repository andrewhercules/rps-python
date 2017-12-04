import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import random
from rps import RockPaperScissorsGame

new_rps_game = RockPaperScissorsGame()

def test_initial_game_status():
    assert(new_rps_game.player_name == '')
    assert(new_rps_game.options == ['rock', 'paper', 'scissors'])
    assert(new_rps_game.player_choice == '')
    assert(new_rps_game.computer_choice == '')

def test_set_player_name():
    new_rps_game.set_player_name('Player')
    assert(new_rps_game.player_name == 'Player')

def test_set_player_choice_rock():
    new_rps_game.set_player_choice('rock')
    assert(new_rps_game.player_choice == 'rock')

def test_set_player_choice_paper():
    new_rps_game.set_player_choice('paper')
    assert(new_rps_game.player_choice == 'paper')

def test_set_player_choice_scissors():
    new_rps_game.set_player_choice('scissors')
    assert(new_rps_game.player_choice == 'scissors')

def test_set_player_choice_unknown_choice():
    assert(new_rps_game.set_player_choice('coffee') == "Error!")

def test_set_computer_choice():
    random.seed(0)
    new_rps_game.set_computer_choice()
    assert(new_rps_game.computer_choice == 'paper')

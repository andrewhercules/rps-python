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

def test_generate_player_choice_string_rock():
    assert(new_rps_game.generate_player_choice_string(1) == 'rock')

def test_generate_player_choice_string_paper():
    assert(new_rps_game.generate_player_choice_string(2) == 'paper')

def test_generate_player_choice_string_scissors():
    assert(new_rps_game.generate_player_choice_string(3) == 'scissors')

def test_set_player_choice_rock():
    new_rps_game.set_player_choice(1)
    assert(new_rps_game.player_choice == 'rock')

def test_set_player_choice_paper():
    new_rps_game.set_player_choice(2)
    assert(new_rps_game.player_choice == 'paper')

def test_set_player_choice_scissors():
    new_rps_game.set_player_choice(3)
    assert(new_rps_game.player_choice == 'scissors')

def test_set_computer_choice():
    random.seed(0)
    new_rps_game.set_computer_choice()
    assert(new_rps_game.computer_choice == 'paper')

def test_determine_winner():
    new_rps_game.set_player_choice(3)
    new_rps_game.determine_winner()
    assert(new_rps_game.winner == 'Player')

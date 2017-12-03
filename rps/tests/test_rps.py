import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from rps import RockPaperScissorsGame

new_rps_game = RockPaperScissorsGame()

def test_initial_game_status():
    assert(new_rps_game.player_name == '')
    assert(new_rps_game.options == ['rock', 'paper', 'scissors'])

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

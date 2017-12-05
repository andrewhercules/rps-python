import random

class RockPaperScissorsGame:

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.player_name = ''
        self.player_choice = ''
        self.computer_choice = ''
        self.winner = ''

    def set_player_name(self, name):
        self.player_name = name

    def set_player_choice(self, player_input_choice):
        if (player_input_choice in self.options):
            self.player_choice = player_input_choice
        else:
            return "Error!"

    def set_computer_choice(self):
        self.computer_choice = random.choice(self.options)

    def determine_winner(self):
        scenarios = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if(self.player_choice == self.computer_choice):
            self.winner += 'draw'
        elif(scenarios[self.player_choice] == self.computer_choice):
            self.winner += self.player_name
        else:
            self.winner += 'computer'
        return

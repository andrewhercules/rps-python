class RockPaperScissorsGame:

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.player_name = ''
        self.player_choice = ''

    def set_player_name(self, name):
        self.player_name = name

    def set_player_choice(self, player_input_choice):
        if (player_input_choice in self.options):
            self.player_choice = player_input_choice
        else:
            return "Error!"

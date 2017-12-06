class Player:

    def __init__(self):
        self.name = ''
        self.choice = ''

    def set_name(self, input_name):
        self.name += input_name

    def set_choice(self, selection):
        choices = ['rock', 'paper', 'scissors'];
        if selection in choices:
            self.choice = selection
        else:
            return 'Error!'

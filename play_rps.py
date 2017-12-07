from rps.rps import RockPaperScissorsGame

new_game = RockPaperScissorsGame()

player_name = input("Welcome to RPS-Python! \nWhat is your name? ")

new_game.set_player_name(player_name)

print("Hello " + new_game.player_name + ". Welcome to Rock, Paper Scissors")

while(new_game.player_choice == ''):
    player_option = input("What option would you like to select - rock, paper, or scissors: ")
    new_game.set_player_choice(player_option)
    if(new_game.player_choice == ''):
        print("Error! Input not valid! Please try again!")
    if(new_game.player_choice != ''):
        print(new_game.player_name + ", you have selected " + new_game.player_choice)
        break

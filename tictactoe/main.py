import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    if (player == computer):
        return "It's a tie!"
    
    return player

choices = get_choices()
print(choices)
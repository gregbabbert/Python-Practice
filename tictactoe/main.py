import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print("You chose " + player)
    print(f"The computer chose {computer}")
    if (player == computer):
        return "It's a tie!"
    elif player == "rock" and computer != "rock":
        if computer == 'scissors':
            return "You win!"
        else:
            return "You lose"
    elif player == "paper":
        if computer == 'rock':
            return "You win!"
        else:
            return "You lose"
    elif player == "scissors":
        if computer == 'paper':
            return "You win!"
        else:
            return "You lose"
    else:
        return "You chose an option we don't recognize"

choices = get_choices()
print(choices)
win = check_win(choices["player"], choices["computer"])
print(win)
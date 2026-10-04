import random
print("Let's play a game of Rock, Paper, Scissors!")
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"You chose {player_choice}. I chose {computer_choice}.")
player_wins = 0
computer_wins = 0
while player_wins < 2 and computer_wins < 2:
    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        winner = "player"
    elif player_choice == computer_choice:
        winner = "tie"
    else:
        winner = "computer"
    if winner == "player":
        player_wins += 1
        print("You win this round!")
    elif winner == "computer":
        computer_wins += 1
        print("I win this round!")
    else:
        print("It's a tie!")
    print(f"Score: You {player_wins} - {computer_wins} Computer")
    if player_wins > computer_wins:
        print("Congratulations! You won the game!")
    else:
        print("I won the game! Better luck next time!")
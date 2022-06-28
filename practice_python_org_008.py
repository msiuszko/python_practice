# gra kamień papier nożyce
import random

while True:
    player1 = input("Enter a choice (rock, paper, scissors): ")
    action = ["rock", "paper", "scissors"]
    player2 = input("Enter a choice (rock, paper, scissors): ")

    if player1 == player2:
        print(f"Both players selected {action}. It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 win!")
        else:
            print("Player 2 win")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 2 win!")
        else:
            print("Player 2 win !")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 win!")
        else:
            print("Player 1 win !")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
# rock, paper, scissors game
import sys
import random

choices = ["ROCK", "PAPER", "SCISSORS"]

def game(games_won=0, games_lost=0, games_tied=0):
    print("ROCK, PAPER, SCISSORS")
    print('%s Wins, %s Losses, %s Ties.' % (games_won, games_lost, games_tied)) 

    # prompt
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        user_input = input()
        if user_input == "q":
            sys.exit()
        elif user_input in ["r", "p", "s"]:
            break
        else:
            print("Invalid input")

    # gets the user's input choice
    if user_input == "r":
        print("ROCK vs ...")
    elif user_input == "p":
        print("PAPER vs ...")
    elif user_input == "s":
        print("SCISSORS vs ...")

    # prints the AI's choice
    ai_choice = choices[random.randrange(0, len(choices))]
    print(ai_choice)

    if user_input == 'r':
        if ai_choice == "ROCK":
            print("TIE!")
            games_tied += 1
        elif ai_choice == "PAPER":
            print("YOU LOSE!")
            games_lost += 1
        else:  # ai_choice == "SCISSORS"
            print("YOU WIN!")
            games_won += 1

    elif user_input == 'p':
        if ai_choice == "ROCK":
            print("YOU WIN!")
            games_won += 1
        elif ai_choice == "PAPER":
            print("TIE")
            games_tied += 1
        else:  # ai_choice == "SCISSORS"
            print("YOU LOSE!")
            games_lost += 1

    elif user_input == 's':
        if ai_choice == "ROCK":
            print("YOU LOSE!")
            games_lost += 1
        elif ai_choice == "PAPER":
            print("YOU WIN!")
            games_won += 1
        else:  # ai_choice == "SCISSORS"
            print("TIE")
            games_tied += 1

    # loops the game
    return games_won, games_lost, games_tied

# runs the game for the first time
games_won, games_lost, games_tied = game()
while True:
    games_won, games_lost, games_tied = game(games_won, games_lost, games_tied)

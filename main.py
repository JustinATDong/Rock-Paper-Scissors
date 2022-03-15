# -*- coding: utf-8 -*-
"""

Justin Dong
CPSC 223P-01
Wed March, 9 2021
donganhtuanjustin@fullerton.edu

"""
import random


gameIsStillLive = True
computerWins = 0
playerWins = 0
ties = 0
#Variable Declaration
while gameIsStillLive:
    playerInput = input("Make your choice: (R, P , S, Q) > ").lower()
    weapon = ['rock', 'paper', 'scissors']
    choices = ['r', 'p', 's', 'q']
    randomWeapon = random.randint(0,2)
    computerChoice = weapon[randomWeapon]

#Checks for user inputs, if they're valid, also prints out the computer's randommized choice
    while playerInput not in choices:
        print("Invalid entry. Try again ")
        userInput = input("Make your choice: (R, P , S, Q) > ").lower()
        
#If player chose Rock
    if playerInput == 'r':
        if computerChoice == 'rock':
            print("Computer chose Rock. Call it a draw.")
            ties += 1
        elif computerChoice == 'paper':
            print("Computer chose Paper. Computer wins.")
            computerWins += 1
        elif computerChoice == "scissors":
            print("Computer chose Scissors. You Win!")
            playerWins += 1

#If player chose Paper
    elif playerInput == 'p':
        if computerChoice == 'rock':
            print("Computer chose Rock. You win")
            playerWins += 1
        elif computerChoice == 'paper':
            print("Computer chose Paper. Call it a draw.")
            ties += 1
        elif computerChoice == "scissors":
            print("Computer chose Scissors. Computer wins.")
            computerWins += 1
            
#If player chose Scissors
    elif playerInput == 's':
        if computerChoice == 'scissors':
            print("Computer chose Rock. Computer wins")
            computerWins += 1
        elif computerChoice == 'paper':
            print("Computer chose Paper. You win!")
            playerWins += 1
        elif computerChoice == "scissors":
            print("Computer chose Scissors. Call it a draw.")
            ties += 1

#If player chooses to quit the game
    elif playerInput == 'q':
        gameIsStillLive = False
        
#Printing the scores
        print(f"Computer: {computerWins}")
        print(f"You: {playerWins}")
        print(f"Ties: {ties}")
        
#Determining who wins the game
if playerWins > computerWins:
    print("You win!")
elif playerWins < computerWins:
    print("Computer won!.")
elif playerWins == computerWins:
    print("You tied!")

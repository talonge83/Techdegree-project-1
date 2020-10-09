"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():

    # Declare variables
    chances = 0
    randomNumber = random.randint(1,10)
    userName = input("What is your name? ")
    bestAttempt = 99999999999
    
    #Display intro/welcome message to the player
    print("Challenger: {}".format(userName))
    print("*********************************************\nWelcome to the Number Guessing Game, {}!\n*********************************************".format(userName))
    
    #Continuously prompt player for a guess    
    while True:
        try:
            playerGuess = int(input("Please guess a number between 1 and 10! "))
        except ValueError:
            print("Not a valid value, please try again..")
            continue
        if playerGuess > 10:
            print("Not a valid value (must be a number between 1 and 10) Please try again..")
            continue
        if playerGuess < randomNumber:
            chances += 1
            print("It's higher")
            if chances == 1:
                print("{} attempt so far!".format(chances))
            else:
                print("{} attempts so far!".format(chances))
            continue
        elif playerGuess > randomNumber:
            chances += 1
            print("It's lower")
            if chances == 1:
                print("{} attempt so far!".format(chances))
            else:
                print("{} attempts so far!".format(chances))
            continue
        else: 
            chances += 1
            currentAttempt = chances
            print("You got it, the number was {}!".format(randomNumber))
            if currentAttempt < bestAttempt:
                #Converts currentAttempt to bestAttempt in the event currentAttempt is lower than previous best.
                bestAttempt = currentAttempt
                print("******************\nNew High Score!: !!({})!!\n******************".format(bestAttempt))                
            else:
                print("No new high score, better luck next time!")            
            chances = 0
            #Prompt user to retry    
            retry = input("Would you like to try again, {}? (YES/NO) ".format(userName))
            if retry.upper() == ("YES" or "Y"):
                print("The current score to beat is {}!".format(bestAttempt))
                randomNumber = random.randint(1,10)
                continue
            else:
                print("Your best score was {}! Thanks for playing, {}!".format(bestAttempt, userName))                
                break




# Kick off the program by calling the start_game function.
start_game()
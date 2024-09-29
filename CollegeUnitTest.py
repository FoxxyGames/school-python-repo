#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

from random import randrange

'''
Generate a random number from a range of 0 to 100
To adjust the range edit the values within the parentheses ()
The first number controls the lower bounds and the second controls the higher bounds
'''
playerplayconf = True
playerresponse = "test"

while playerplayconf == True:
    random_number = randrange(0, 100)
    #print(random_number) //Test code to ensure random value properly generates.

    print("Guess the random number in 10 tries (integers only)!")

    failed = False
    guess_count = 1
    guess = input("\nGuess #1. Enter your first guess:      ")

    while int(guess) != random_number:
        if int(guess_count) == 10:
            print("Sorry, you lose! The correct number was: " + str(random_number))
            failed = True
            break
        else: 
            print("Oops! Wrong number! Please try again!")
            if int(guess) > int(random_number):
                print("Here's a hint! Your number was bigger then the number I chose!")
            else:
                print("Here's a hint! Your number was less then the number I chose!")
            guess_count = guess_count + 1
            guess = input("\nGuess #" + str(guess_count) + ". Guess your next guess:    ")

    if failed == False:
        print("Good job! The number was indeed " + str(guess) +  "! It only took you " + str(guess_count) + " tries to get it!")

    playerresponse = input("Would you like to play again? (y/n):        ")

    while playerresponse != str("y") and playerresponse != str("n"):
        print("Invalid response! Please try again!")
        playerresponse = input("Would you like to play again? (y/n):        ")

    if playerresponse == "y":
        playerplayconf == True
        guess_count = 1
        failed = False
    else:
        playerplayconf == False
        print("\nThank you for playing my game!")
        print("Created by: Jasmine Matthews")
        break

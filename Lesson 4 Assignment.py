#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

from random import randrange
# debughack = True # // Remenents of Debugging Functionality
                   # // Allows developer to hijack enemy's choice for testing purposes.
def GetUserWeapon(): # // Lets player decide upon their weapon.
    print("SELECT YOUR WEAPON (1-3)") # // These could be merged into one print string.
    print("------------------------") # // For sake of readability it will just remain as this.
    print("1. Rock")                  # // But I wanted to point out that potential optimization.
    print("2. Paper")
    print("3. Scissors")
    playerchoice = input("Select your Weapon: ")
    return playerchoice

def GetEnemyWeapon(): # // Randomly decides the enemy's weapon and prints an appropriate string.
    #if debughack == True: # // Execution Code for overriding AI value.
    #    enemychoice = 3
    #else:
    enemychoice = randrange(1,3)
    if enemychoice == 1:
        print("I choose Rock!")
    elif enemychoice == 2:
        print("I choose Paper!")
    elif enemychoice == 3:
        print("I choose Scissors!")
    return enemychoice

def DeclareWinner(playerinput, enemyinput): # // Declares the winner based on the results.
    # print(str(playerinput)) //Debugging Strings during testing
    # print(str(enemyinput))
    # int(playerinput) 
    # int(enemyinput)
    
    if int(playerinput) == int(enemyinput): # // For some reason, Python was extremely fussy with this area of
        print("Its a tie!")                 # // the code, and the constant "int(variable)" tactic was the only
    elif int(playerinput) == 1 and int(enemyinput) == 3: # // way I got to fix it. There definately is a 
        print("Your rock crushed my scissors, you win!") # // solution for it, but it at least works.
    elif int(playerinput) == 3 and int(enemyinput) == 2:
        print("Your scissors cut my paper, you win!")
    elif int(playerinput) == 2 and int(enemyinput) == 1:
        print("Your paper covered my rock, you win!")
    elif int(playerinput) == 3 and int(enemyinput) == 1:
        print("My rock crushed your scissors, you lose!")
    elif int(playerinput) == 1 and int(enemyinput) == 2:
            print("My paper covered your rock, you lose!")
    elif int(playerinput) == 2 and int(enemyinput) == 3:
            print("My scissors cut your paper, you lose!")

def main(): # // Main Function for the code.
    # print("WORK IN PROGRESS")
    playercontinue = True
    while playercontinue == True:
        playerweapon = GetUserWeapon()
        enemyweapon = GetEnemyWeapon()
        DeclareWinner(playerweapon, enemyweapon)
        playerresponse = input("Would you like to play again? (y/n):        ") # // Lets player choose to continue.
        while playerresponse != str("y") and playerresponse != str("n"):
            print("Invalid response! Please try again!")
            playerresponse = input("Would you like to play again? (y/n):        ")

        if playerresponse == "y":
            playercontinue == True
        else:
            playercontinue == False
            print("\nThank you for playing my game!")
            print("Created by: Jasmine Matthews")
            break


if __name__ == "__main__":
    main()

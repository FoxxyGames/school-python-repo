#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing, as per usual. Wheeeeeee!

def main(): # // Main Function for the code.
    print("Work In Progress") # // Starting debug line my peciousssss
    print("Welcome to the String Replacement tool!")
    printborder(39)
    ExitingProgram = False
    InputData = []
    ReinputSetting = 0 # // 0 = Null/1 = Edit String 1/2 = Edit String 2/3 = Edit Both/4 = Exit Program
    while ExitingProgram == False: # // Added this extra customization cuz I thought it would be easy and I was bored.
        ReinputData = []           # // Its nice, but kinda garbagely coded cuz my brain doesnt work. Could be better.
        NewInputData = GetInputs(ReinputSetting)
        if ReinputSetting == 0 or ReinputSetting == 1 or ReinputSetting == 3:
            ReinputData.append(NewInputData[0])
        else:
            ReinputData.append(InputData[InputData])
        if ReinputSetting == 0 or ReinputSetting == 2 or ReinputSetting == 3:
            ReinputData.append(NewInputData[1])
        else:
            ReinputData.append(InputData[InputData])
        InputData = ReinputData # // Final data is compiled into this variable.
        print("\nSearching for substring within the string content, please wait!")
        printborder(60)
        IndexFound = SearchForSubstring(InputData) # // Run Search Code
        # print(IndexFound) // Old Test Code
        if IndexFound == -1: # // Checks if the user's input is garbage.
            print("Couldnt find the substring within the main string! What do you want to try to do?")
            InInputLoop = True
            while InInputLoop == True:
                ReInputSetting = input("1 = Edit String To Search Through, 2 = Edit String To Search For, 3 = Edit Both, 4 = Exit Program: ")
                if ReInputSetting == "1" or ReInputSetting == "2" or ReInputSetting == "3":
                    InInputLoop = False
                if ReInputSetting == "4": # // Quit Program
                    InInputLoop = False
                    print("Thank you for using the program!")
                    credits()
                    ExitingProgram = True
                else: # // Tell user to try again.
                    print("Invalid Entry, please try again!")
        else: # // Runs if the user's input is actually usable.
            AwaitingConf = True
            while AwaitingConf == True:
                PlayerResponse = input("\n" + ReinputData[1] + " was found in the string at index " + str(IndexFound) + ". Wanna replace it? (y/n) ")
                if PlayerResponse == "n": # // If user doesnt wanna replace the string, run this!
                    print("Okay then, thank you for using the program!")
                    printborder(20)
                    credits()
                    AwaitingConf = False
                    ExitingProgram = True
                if PlayerResponse == "y": # // If they wanna run it, then run this!
                    # print("To-Do: Implement") // Old To-Do Marker
                    print("\nInitializing the string replacement process!")
                    printborder(60)
                    ReplacementString = input("Enter the replacement string: ")
                    NewString = ReplaceSubString(InputData[0],InputData[1],ReplacementString)
                    print("\nNew String: " + NewString)
                    print("\nThank you for using the program!")
                    printborder(20)
                    credits()
                    AwaitingConf = False
                    ExitingProgram = True
                else: # // Tell the user to give a normal response.
                    print("Please type in a valid response")



def GetInputs(InputSetting): # // Fetch the user's data.
    if int(InputSetting) == 0 or InputSetting == 1 or InputSetting == 3:
        StartingString = input("Enter the string to search through: ")
    else: # // These Else statements and Dummy fillers are probably not nessesary, but its best to be safe and avoid any potential bugs.
        StartingString = "Dummy"
    if int(InputSetting) == 0 or InputSetting == 2 or InputSetting == 3:
        StringToFind = input("Enter the string to search for:")
    else:
        StartingString = "Dummy"
    AssembledData = [StartingString, StringToFind] # // Assemble the data to ship to Main.
    return(AssembledData)

def SearchForSubstring(Inputs): # // Search for and obtain the new substring the user wants to replace.
    StartString = Inputs[0]
    SearchForString = Inputs[1]
    FoundIndex = StartString.find(SearchForString)
    return(FoundIndex)


def ReplaceSubString(MainString, OldSubString, NewSubString): # // Replace the old Substring with the new Substring
    UpdatedString = MainString.replace(OldSubString,NewSubString)
    return(UpdatedString)

def credits():
    print("Completed by, Jasmine Matthews")

def printborder(BorderLength): # // Updated this to feature more customization. Could maybe be handled better?
    BorderText = ""
    for i in range(int(BorderLength)):
        if BorderLength != 0:
            BorderText = BorderText + "-"
    print(BorderText)

if __name__ == "__main__":
    main()
#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

import random

def main(): # // Main Function for the code.
    # print("WORK IN PROGRESS")
    grades_list = getgrades()
    print("Removing the lowest grade")
    grades_list = removelowestgrade(grades_list)
    print(grades_list)
    print("Removing random grade")
    grades_list = removerandomgrade(grades_list)
    print(grades_list)
    editgrade(grades_list)




def getgrades():
    CanExit = False
    grades_list_temp = []
    currentgrade = 0
    current_grade_ID = 0
    while CanExit == False:
        currentgrade = input("Input a grade you wish to use or type -1 to stop:    ")
        if int(currentgrade) == -1:
            CanExit = True
        else:
            grades_list_temp.insert(current_grade_ID,int(currentgrade))
            current_grade_ID = current_grade_ID + 1
    print(grades_list_temp)
    return grades_list_temp

def removelowestgrade(grades_list):
    # print("test")
    # print(grades_list.index(min(grades_list)))
    grades_list.pop(grades_list.index(min(grades_list)))
    return grades_list

def removerandomgrade(grades_list):
    randomitem = random.choice(grades_list)
    grades_list.remove(randomitem)
    return(grades_list)

def editgrade(grades_list):
    print("Edit a grade")
    currentindex = 0
    gradetoedit = 0
    for loop in range(0,len(grades_list)):
        print(int(currentindex) + 1, ". ", grades_list[currentindex])
        currentindex = currentindex + 1
    gradevalid = False
    while gradevalid == False:
        gradetoedit = input("What grade do you want to edit: ")
        if int(gradetoedit) > len(grades_list) or gradetoedit == 0:
            print("Please enter a valid grade!")
        else:
            gradevalid = True
            break
    newgrade = input("Enter the new grade: ")
    # print(gradetoedit)
    grades_list.pop(int(gradetoedit) - 1)
    grades_list.insert(int(gradetoedit) - 1, int(newgrade))
    print(grades_list)
    print("Unable to Sort and Reversing List")
    # grades_list2 = grades_list               //No matter what I do nothing here works
    # grades_list = grades_list.sort           //It always gives me a message seemingly
    # print(grades_list)                       //Calling the build in method, without
    # grades_list2 = grades_list.reverse       //Doing anything. I need to submit this.
    # print(grades_list2)                      //But there's nothing I can do.
    ReturnClassTotal(grades_list)           #  //Error code attached in Document
    ReturnClassAverage(grades_list)
    PrintCredits()


def ReturnClassTotal(grades_list):
    print("Total: ", sum(grades_list))

def ReturnClassAverage(grades_list):
    print("Class Average: ", sum(grades_list) / len(grades_list))

def PrintCredits():
    print("Completed by Jasmine Matthews.")

if __name__ == "__main__":
    main()
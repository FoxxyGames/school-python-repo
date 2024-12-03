#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

from random import randrange

def main(): # // Main Function responsible for all the main stuff.
    # print("WORK IN PROGRESS")
    print("Organization Employee Log")
    print("======================================")
    Employee_Input_Amount = input("\nHow many new employees are you adding: ")
    print("\n======================================")
    Employee_Dictionary = AddNewEmployees(Employee_Input_Amount)
    PrintUserInformation(Employee_Dictionary)

def AddNewEmployees(Employee_Count):
    Employee_List = [] # // This whole Function adds all the new employees the array.
    Employee_ID_List = []
    Current_Employee_Valid = False
    for Count in range(int(Employee_Count)): # // For each employee, perform the add employee request operation.
        while Current_Employee_Valid == False: # // Check to make sure the employee is valid and add it to the array if allowed.
            Current_Employee = input("Enter Employee Name: ").title()
            if Employee_List.count(Current_Employee) == 0 :
                Current_Employee_Valid = True
            else:
                Current_Employee_Valid = False
                print("Error: Employee Already Exists")
        Employee_List.append(Current_Employee)
        print("======================================")
        Current_Employee_Valid = False
        while Current_Employee_Valid == False: # // This creates the ID List, whilst still making sure the ID generated is valid.
            Current_Employee_ID = randrange(1,500)
            if Employee_ID_List.count(Current_Employee_ID) == 0:
                Current_Employee_Valid = True
                Employee_ID_List.append(Current_Employee_ID)
            else:
                Current_Employee_Valid = False
        Current_Employee_Valid = False
    CurrentEmployeeInloop = 0
    Employee_Dictionary = {}
    for Employee in Employee_List: # // Turns the two lists into a dictionary
        Employee_Dictionary.update({Employee: Employee_ID_List[CurrentEmployeeInloop]})
        CurrentEmployeeInloop = CurrentEmployeeInloop + 1
    # print(Employee_Dictionary) // Debugging String to make sure this garbage works.
    return(Employee_Dictionary)

def PrintUserInformation(EmployeeData): # // Prints all the information from the Dictionary along with the credit.
    print("\nCreated User Information")
    for Key in EmployeeData:
        print("======================================")
        print("Created Employee:\t" + Key)
        print("EmployeeID:\t\t" + str(EmployeeData[Key]))
    print("\n======================================")
    print("Created by, Jasmine Matthews")

if __name__ == "__main__":
    main()
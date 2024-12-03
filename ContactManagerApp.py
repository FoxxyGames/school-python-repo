#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing, as per usual. Teeheehee

# // Default Path Location : C:\Users\Default\Documents\filename.txt

# // This is probably the stinkiest thing anybody could have made. Good. God.
# // This all hopefully works, but either way its all 99% Garbage.

import csv

def main(): # // Main Function for the code.
    FileTestingToggle = False # // Enabling this wil run the File Test Function used for experimenting
    # debugmode = True # // Unused Debugging Code
    if FileTestingToggle == True:
        filetestfunction()
    else:
        stillusingprogram = True
        # print("WORK IN PROGRESS")
        print("Welcome to the Contact Manager App!")
        borderprint()
        while stillusingprogram == True: # // The main segment for programming
            chosenprimaryoption = getplayeroption()
            # // print(chosenprimaryoption) # // Debug to make sure those base functions work
            borderprint()
            if int(chosenprimaryoption) == 1:
                CreateNewContactFile()
            elif int(chosenprimaryoption) == 2:
                AddNewContact()
            elif int(chosenprimaryoption) == 3:
                ViewAllContacts()
            elif int(chosenprimaryoption) == 4:
                ModifyExistingContact()
            elif int(chosenprimaryoption) == 5:
                credits()
                stillusingprogram = False
            else:
                print("Improper input, please try again!")

def borderprint(): # // Thought it better to make this its own function to make it easier to adjust the borders if nessesary.
    print("-----------------------------------")

def getplayeroption(): # // Prints the options, could have these be one print function instead of several, 
    print("\nPush one of the following options to perform the corresponding action:") # // but for now this will work.
    print("1 - Create new contact file")
    print("2 - Add new contact")
    print("3 - View all contacts")
    print("4 - Modify an existing contact")
    print("5 - Save and exit")
    selection = input("Enter your selection:")
    return selection

def CreateNewContactFile(): # // Just creates the inital code
    with open("contacts.csv", "w") as f:
        writer = csv.writer(f)
    print("\nContact file successfully created!\n")
    borderprint()

def AddNewContact(): # // This is responsible for adding a new contract. Its done terribly, but it "works"
    contactname = input("Enter the contact name:")
    contactphonenumber = input("Enter contact phone number:")
    contactemail = input("Enter contact email address:")
    # contactfull = [contactname, contactphonenumber, contactemail] # // Old Stupid Garbage
    contactfull = {"Contact Name": contactname,
             "Contact Phone Number": contactphonenumber,
             "Contact Email": contactemail}
    # print(contactfull)
    with open("contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([contactfull])
    #     writer.writerow(contactname)
    #     writer.writerow(contactphonenumber)
    #     writer.writerow(contactemail)

    print("Contact added successfully!\n")
    borderprint()

def ViewAllContacts(): # // Just prints all the contact information contained
    print("\nContacts Information:")
    borderprint()
    print("Name\t\tPhone\t\t\tEmail")
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            Vartest = row[0]
            VarTest2 = eval(Vartest)
            # print(VarTest2)
            print(VarTest2.get("Contact Name"), "\t\t", VarTest2.get("Contact Phone Number"), "\t\t", VarTest2.get("Contact Email"))
    borderprint()

def ModifyExistingContact(): # // As a rockstar games programmer said in the past "this is ugly as **** but I dont care."
    ViewAllContacts() # // All of this code modifies the existing contract and just redoes it.
    KickedOut = False
    while KickedOut == False:
        successvar = False
        PersonToEdit = input("\nEnter the name of the contact you want to modify:")
        completearray = []
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                Vartest = row[0]
                VarTest2 = eval(Vartest)  # // This was the only way I could get this garbage working. Just converts the thing.
                # completearray.append(VarTest2)
                if VarTest2.get("Contact Name") == PersonToEdit:
                    successvar = True
                    # print("Worked!")
                    KickedOut = True
                    print("\nCurrent Details: Name: " + VarTest2.get("Contact Name") + ", Phone: " + VarTest2.get("Contact Phone Number") + ", Email: " + VarTest2.get("Contact Email"))
                    NewPhoneNumber = input("Enter new phone number (leave blank to keep current): ")
                    if NewPhoneNumber == "":
                        NewPhoneNumber = VarTest2.get("Contact Phone Number")
                    NewEmailAddress = input("Enter new email address (leave blank to keep current): ")
                    if NewEmailAddress == "":
                        NewEmailAddress = VarTest2.get("Contact Email")
                    NewContactFull = {"Contact Name": VarTest2.get("Contact Name"),
                        "Contact Phone Number": NewPhoneNumber,
                        "Contact Email": NewEmailAddress}
                    completearray.append(NewContactFull)
                else:
                    completearray.append(VarTest2)
            if successvar == False:
                print("Not a valid person! Try again!")
                completearray = []
            else:
                # print("Fuck")
                # print(completearray)
                with open("contacts.csv", "w") as f:
                    writer = csv.writer(f)
                with open("contacts.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    for item in completearray:
                        # print(item)
                        writer.writerow([item])
                    # writer.writerow("test")
                    # writer.writerow(completearray)

def filetestfunction(): # // Testing function for tinkering with files. Just a little playground of sorts.
    print("This is for testing files. If your calling this, then stop calling it.")
    file = open("my_file.txt", "w")
    file.close()
    students_testvar = [
      ["Jake", "100"],
      ["Steve", "90"],
      ["John", 95]
    ]
    with open("test.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students_testvar)
    
def credits():
    print("Completed by, Jasmine Matthews")

if __name__ == "__main__":
    main()
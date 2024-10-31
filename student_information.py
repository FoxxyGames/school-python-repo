#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

def main(): # // Main Function for the code.
    dictionarytest = {
        "Jack":
            {"StudentID": "143986",
             "GPA": "3.2",
             "CreditsCompleted": "88.4",
             "Grades": "[92, 98, 89, 96]"},
        "Lana":
            {"StudentID": "204863",
             "GPA": "3.9",
             "CreditsCompleted": "94.2",
             "Grades": "[90, 76, 84, 96, 89, 98]"},
        "Sammy":
            {"StudentID": "420198",
             "GPA": "2.1",
             "CreditsCompleted": "15.2",
             "Grades": "[1, 52, 98, 16]"}
    }
    print(dictionarytest)

    print("\nList of Students")
    for key in dictionarytest:
        print(key)
    
    print("\nStudent Information")
    print("Student\t ID\t\t GPA\t Credits Completed\tGrades")
    for key in dictionarytest:
        printtitle(dictionarytest[key], key)
    
    print("\nAccessing Student Information Using the Key in a Loop")
    printallcurrentstudents(dictionarytest)
    
    print("\nSammy has dropped out, removing from student info registry")
    dictionarytest = removestudent("Sammy", dictionarytest)
    printallcurrentstudents(dictionarytest)
    getstudentgpa("Lana", dictionarytest)
    clearinformation(dictionarytest)
    print(dictionarytest)
    print("Completed by Jasmine Matthews")

def printtitle(content, name):
    print(name, "\t", content.get("StudentID"), "\t", content.get("GPA"), "\t", content.get("CreditsCompleted"), "\t\t\t", content.get("Grades"), "\t", )

def removestudent(name, dictionary): # // Allows for the removal of a student
    dictionary.pop(name)
    return (dictionary)

def printallcurrentstudents(dictionary):
    for key in dictionary:
        print(key, (dictionary[key]))

def getstudentgpa(student, dictionary):
    print("\nGetting", student, "'s GPA")
    placeholder = dictionary.get(student)
    # print(placeholder)
    print(placeholder.get("GPA"))

def clearinformation(dictionary):
    print("\nStudents have graduated, yay! Clearing the student registry.")
    dictionary.clear()
    return dictionary

if __name__ == "__main__":
    main()
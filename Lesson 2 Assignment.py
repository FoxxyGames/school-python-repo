#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

first_name = "Placeholder"
last_name = "Placeholder"
birth_year = 2000
current_year = 2000
finalcalc = 2000

print("Age Calculator 2000")

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

birth_year = input("Enter your birth year: ")

current_year = input("Enter the current year: ")

finalcalc = int(current_year) - int (birth_year)

print("\nHello there " + first_name + " " + last_name + "!")

print("Wow " + first_name + "! Your " + str(finalcalc) + " years old!")

print(f"\nNext year your gonna be {finalcalc + 1} years old! Cool right?")

print("\nThank you", first_name, last_name, "for participating in this test!")

print("---------------------------\nWritten by Jasmine Matthews")

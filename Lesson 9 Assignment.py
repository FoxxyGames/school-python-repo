#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing, as per usual. Wheeeeeee!

def main(): # // Main Function for the code.
    # print("Work In Progress") // Got our usual starting code here that is commented out. He serves us well every time. Salute to mister Work In Progress Printer.
    PerformCheck = True # // Multiuse Variable my beloved. Used for both this while loop and the next one.
    while PerformCheck == True:
        try:
            TotalIncome = input("Enter your total income: $")
            if float(TotalIncome) < 0: # // Check if negative. If negative, harass user.
                raise ValueError("Invalid Input: Income cannot be negative. Please enter a valid income amount.")
            else:
                PerformCheck = False
                break # // Yippee we got our money! Break the While Loop.
        except ValueError as e: # // Check for errors
            print(f"Invalid Input: {e}. Please enter valid income amount.") 
        except Exception as e:
            print(f"Invalid Input: {e}. Please enter valid income amount.")
    PerformCheck = True # // Initalize these three variables
    TotalExpenses = 0
    ExpenseList = []
    while PerformCheck == True:
        try:
            ExpenseAmount = input("Enter an expense amount: $")
            if float(ExpenseAmount) == 0:
                PerformCheck = False
                break # // Done entering numbers? Great! Do a break!
            if float(ExpenseAmount) < 0: # // Check if negative. If negative, harass user.
                raise ValueError("Invalid Input: Expense cannot be negative. Please enter a valid expense amount.")
            else:
                ExpenseList.append(ExpenseAmount) # // Append to list and add to total expenses.
                TotalExpenses = TotalExpenses + float(ExpenseAmount)
        except ValueError as e:  # // Check for errors
            print(f"Invalid Input: {e}. Please enter valid expense amount.")
        except Exception as e:
            print(f"Invalid Input: {e}. Please enter valid expense amount.")
    PrintResults(TotalIncome,ExpenseList,TotalExpenses)
    credits()

def PrintResults(TotalIncome,ExpenseList,TotalExpenses): # // Responsible for printing all the results
    RemainingBudget = float(TotalIncome) - float(TotalExpenses)
    print("Budget Results:")
    printborder()
    print(f"Total Income: ${float(TotalIncome):.2f}")
    print(f"Total Expenses: ${float(TotalExpenses):.2f}")
    print(f"Remaining Budget: ${float(RemainingBudget):.2f}")
    printborder()
    print("Complete Expense List")
    printborder()
    for item in ExpenseList: 
        print(f"{ExpenseList.index(item)}. ${float(item):.2f}")


def credits():
    print("Completed by, Jasmine Matthews")

def printborder():
    print("---------------------------")

if __name__ == "__main__":
    main()

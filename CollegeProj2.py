#! /usr/bin/etc python3
# Hello! I'm a hidden lil thing mwahahahahaha

investment_amount = 1
interest_rate = 1
investment_duration = 1
invesement_compounded_monthy = 12
year_by_year_results = 12
months_count = 12
future_total = 0
interest_temp = 0
current_year = 0

investment_amount = input("Enter the investment amount (must be greater then 0 but less then 50000): ")

while int(investment_amount) < 0 or int(investment_amount) > 50000:
    print ("Your number isnt in range, please try again!")
    investment_amount = input("Enter an investment that is greater then 0 but less then 50000: ")

interest_rate = input("Enter the interest rate (must be greater then 0 but less then 15): ")

while int(interest_rate) < 0 or int(interest_rate) > 15:
    print ("Your number isnt in range, please try again!")
    interest_rate = input("Enter an interest rate that is greater then 0 but less then 50000: ")

investment_duration = input("Enter the investment duration in years: ")

while int(investment_duration) <= 0:
    print ("Your number isnt in range, please try again!")
    investment_duration = input("Enter an investment duration that is at least 1 year long: ")

invesement_compounded_monthy = (float(interest_rate) / 12) / 100

months_count = int(investment_duration) * 12

for month in range (months_count):
    future_total = float(future_total) + float(investment_amount)
    interest_temp = future_total * invesement_compounded_monthy
    interest_temp = round(interest_temp, 2)
    future_total = round(future_total + interest_temp,2)
    if int(month) - (int(current_year) * 12) == 11:
        current_year = int(current_year) + 1
        print ("Year " + str(current_year) + ": $" + str(future_total)) 

print ("\nInvestment Duration: " + str(investment_duration) + " years")
print ("Yearly Interest Rate: " + str(interest_rate) + ".0%")
print ("Monthly Investment Amount: $" + str(investment_amount))
print ("Total Amount of Investment After Compounding: $" + str(future_total))
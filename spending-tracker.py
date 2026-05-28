from datetime import datetime as dt
from decimal import Decimal

#Prints date, with formatting for accurate suffixes
def print_date():
    if(int('%d' == 1) or int('%d' == 21) or  int('%d' == 31)): 
        today_str = dt.now().strftime('%A') + ", " + dt.now().strftime('%B %d') + "st" 
    elif(int('%d' == 2) or int('%d' == 22)):
        today_str = dt.now().strftime('%A') + ", " + dt.now().strftime('%B %d') + "nd" 
    elif(int('%d' == 3) or int('%d' == 23)):
        today_str = dt.now().strftime('%A') + ", " + dt.now().strftime('%B %d') + "rd"       
    else:
        today_str = dt.now().strftime('%A') + ", " + dt.now().strftime('%B %d') + "th"
    print("Today is " + today_str)

#Collects user input and stores in dictionary
def user_data():
    pay_timeframe = input("How often are you paid? (Weekly/Biweekly): ")
    pay_date = input("When is your payday? (Day of the week): ")
    budget = Decimal(input("What is your weekly budget goal? (Include decimals): "))

    user_data = {}
    user_data['budget_length'] = "Weekly"
    user_data['pay_freq'] = pay_timeframe
    user_data['payday'] = pay_date
    user_data['budget_amt'] = budget

    print(user_data)
    return user_data
    #TO DO: edge case logic           

#Computes budget as user inputs values, assuming user inputs one large sum at the end of the day
def budget_calculator(date, payday, pay_freq, budget_length, budget_amt, weekly_total, monthly_total):
    money_spent = Decimal(input("Enter amount spent: "))
    
    if (date == payday):
        weekly_total = 0
        weekly_total += money_spent
    else:
        weekly_total += money_spent
   
    monthly_total += money_spent
   
    return weekly_total, monthly_total


print("***************************************************************")
intro = """Hi! Im your new spending tracker! I will help you stay under a budget you set based 
on a series of questions. With the information you provide, I will be able to help you stick to 
your financial goals. I will also provide a monthly overview of what you spent and where, helping
you further monitor your spending habits."""

print(intro)
start = input("Ready to start? [Y/N]: ")

current_user_data = user_data()
current_weekly_total = 0
current_monthly_total = 0

current_weekly_total, current_monthly_total = budget_calculator(**current_user_data, weekly_total = current_weekly_total, monthly_total = current_monthly_total)

if start == "Y" or start == "y":
    print("***************************************************************")
    today_str = dt.now().strftime('%A') + ", " + dt.now().strftime('%B %d')

    print("Today is " + today_str)

elif start == "N" or start == "n":
    print("Goodbye.")
else:
    while start != "Y" or start != "N":
        start = input("Please input a valid character [Y/N]: ")
        if start == "Y" or start == "y":
            print("***************************************************************")
            print("Welcome.")
            break
        elif start == "N" or start == "n":
            print("Goodbye.")
            break
"""
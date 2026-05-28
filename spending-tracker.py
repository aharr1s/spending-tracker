
def calculate_total(money_spent):
    weekly_total = weekly_total + money_spent
    day_counter = day_counter + 1
   
    monthly_total = money_spent + monthly_total
    return monthly_total

def budget_overview(calculate_total):
    

def main():
    
   
    money_spent = input("Enter money spent: ")
    money_spent = float(money_spent)
    day = input("Enter day of week: ")
    calculate__total(money_spent)


if __name__ == "__main__":
    main()
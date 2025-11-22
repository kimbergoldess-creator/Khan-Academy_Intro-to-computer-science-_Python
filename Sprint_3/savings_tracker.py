savings_goal = 1800
saved_amount = 0
month = 0
monthly_amount = 0

for month in range(1,13):
    saved_amount = float(input("How much have you saved in month " + str(month) + "... "))
    monthly_amount += saved_amount
    if monthly_amount < savings_goal and month < 12:
        print("You now have " + str(monthly_amount) + " $")
        print("Not quite there, see you next month")
    elif monthly_amount < savings_goal and month == 12:
        print("Almost, you saved " + str(monthly_amount) + " in " + str(month) + " months.")
    else:
        print("You reached your goal of " + str(savings_goal) + " in month " + str(month))
        print("Your spared in total " + str(monthly_amount) + " in just " + str(month) + " months! Good job!")
        break

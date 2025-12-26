basic_wage = 12.50
extra_wage = 18.75
hours_worked = 0
max_hours_x_shift = 12
total_wage = 0

for day in range(1,6):
    hours_worked = float(input("How many hours have you worked in shift " + str(day) + "? "))
    shift_wage = float(hours_worked * basic_wage)
    extra_hours_wage = float((max_hours_x_shift - hours_worked) * extra_wage)
    total_wage += shift_wage
    if hours_worked >= 0 and hours_worked <= 8:
        print("Your wage for shift " + str(day) + " is " + str(shift_wage) + " $.")
    elif hours_worked > 8 and hours_worked <= 12:
        print("Your wage for shift " + str(day) + " is " + str(shift_wage + extra_hours_wage) + " $.")
    else:
        print("Policy error")
        break
print("----------------------------------------------")
print("Total wage for " + str(day) + " days is " + str(total_wage) + " $.")

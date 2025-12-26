goal_weight = 75.0
current_weight = 86.0 
week = 0

while current_weight > goal_weight:
    week += 1
    current_weight = float(input("What's your weight for week " + str(week) + " "))
    if current_weight > goal_weight:
      print("Not quite there yet, see you next week. ")
    else:
      print("----------------------------------------------------------------------")
      print("Congratulations! You reached your goal of " + str(goal_weight) + " kg at week " + str(week) + "!")

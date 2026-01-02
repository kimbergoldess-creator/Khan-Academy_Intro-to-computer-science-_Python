def get_total_reps(sets, reps_per_set):
    """Calculates total repetitions."""
    reps = sets * reps_per_set
    return reps

def get_weight_lifted(reps, weight):
    """Calculates total weight lifted."""
    weight_lifted = reps * weight
    return weight_lifted

def calculate_workout_volume(sets, reps_per_set, weight):
    """Calculates the total volume of an exercise."""
    total_reps = get_total_reps(sets, reps_per_set)
    calculated_weight = get_weight_lifted(total_reps, weight)
    return calculated_weight

total_volume = calculate_workout_volume(4, 10, 15)

print("Total volume for this exercise: " + str(total_volume) + " kg")

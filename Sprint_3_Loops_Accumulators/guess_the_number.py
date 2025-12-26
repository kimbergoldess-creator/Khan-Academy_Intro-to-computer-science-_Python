# Guessing Game: Basic Implementation

# --- Setup and Initialization ---
import random 

# Generates a random integer between 1 and 100 (inclusive).
# This is the target number the user must guess.
secret_num = random.randint(1, 100)

# Initializes the user's guess variable.
# Set to 0 to ensure the 'while' loop starts correctly 
# (since 0 is outside the 1-100 range).
guess = 0

# --- Main Game Loop ---
# The loop continues as long as the user's guess does not match the secret number.
while guess != secret_num:
    # 1. Prompt for input and convert the string input to an integer.
    # This line also updates the 'guess' variable, controlling the loop condition.
    guess = int(input("Guess the secret number! "))
    
    # 2. Provide feedback to the user based on the guess.
    
    # If the guess is too high:
    if guess > secret_num:
        print("Too high, try again! ")
        
    # If the guess is too low:
    elif guess < secret_num:
        print("Too low, try again! ")
        
    # 'else' executes only when guess == secret_num, breaking the loop.
    else:
        print("You win!")

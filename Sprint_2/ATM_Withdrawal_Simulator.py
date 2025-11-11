balance = float(input("Enter your balance "))

if balance > 0:
    # Withdrawal request and check happen only here (Nesting)
    withdrawal = float(input("Enter the withdrawal amount "))
    
    if balance > withdrawal:
        print("Withdrawal granted ")
    elif balance < withdrawal:
        # Note: Using 'else' would be cleaner here (as discussed), but 'elif' is functional
        print("Insufficient funds ")
else:
    # Non-positive balance error
    print("Your balance is zero or negative. Withdrawal denied ")

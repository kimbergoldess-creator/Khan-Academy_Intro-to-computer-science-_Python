permission = str(input("Do you want to proceed S/N "))
required_space = 4.5

if permission.upper() == "S":
    # Enter here only if permission is granted
    available_space = float(input("Enter available disk space in GB "))
    
    if available_space >= required_space:
        print("Download and installation initiated. ")
    elif available_space < required_space:
        print(f"Insufficient disk space. Free up {required_space} GB.")
        
elif permission.upper() == "N":
    # Case where the user denies the update
    print("Update cancelled by user.")
    
else:
    # Case where the input is different from S or N
    print("Check that you have entered S or N")

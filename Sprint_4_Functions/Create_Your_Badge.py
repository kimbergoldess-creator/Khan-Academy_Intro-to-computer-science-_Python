def get_uppercase_name(name):
    """Returns the name in uppercase."""
    upper_name = name.upper()
    return upper_name

def get_code_format(specialty):
    """Formats the specialty in uppercase and brackets."""
    upper_specialty = specialty.upper()
    return "[" + upper_specialty + "]"

def create_badge(name, specialty):
    """Generates the full agent badge by combining name and specialty."""
    clean_name = get_uppercase_name(name)    
    formatted_specialty = get_code_format(specialty)    
    return clean_name + " - " + formatted_specialty

# --- Main Program ---

# Collect user input
name = input("What's your name? ")
specialty = input("What's your specialty? ")

# Generate the badge string
my_badge = create_badge(name, specialty)

# Normalize specialty for the security check
specialty_upper = specialty.upper()

# Security filter: block any specialty containing "HACK"
if "HACK" in specialty_upper:
    print("Access Denied. Threat detected.")
else:
    print("Agent Access Granted: " + my_badge)

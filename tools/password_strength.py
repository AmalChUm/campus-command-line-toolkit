import getpass

AUTHOR = "Merve Filiz Baker"
APP_NAME = "Password Strength Checker"

def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    score = sum([has_lower, has_upper, has_digit, has_special])
    
    if length < 8 or score < 2:
        return "Weak"
    elif length >= 12 and score >= 3:
        return "Strong"
    else:
        return "Moderate"

def run():
    print(f"--- {APP_NAME} (Educational Only) ---")
    try:
        password = getpass.getpass("Enter password to check: ")
        if not password:
            print("Error: Password cannot be empty.")
            return
        
        strength = check_strength(password)
        print(f"Password Strength: {strength}")
        print("Note: This tool is for educational purposes only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run()
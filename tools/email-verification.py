import re

AUTHOR = "Gaige Szy"
APP_NAME = "Email Verification Tool"

def run():
    """This program will verify if an email address is valid."""
    
    valid = False #used to change while loop state based on the verification result
    while not valid:
        email = input("Enter an email address to verify, or type exit to quit: ").strip() #used to gather input from user, strips whitespace

        if email == "exit" or email == "EXIT":
            # Allows users an option to pass over the program
            print("Exiting the email verification tool.\n")
            break

        # Regex pattern splits on substrings "@", ".com", ".org", ".net", ".edu", ".gov"
        separations = re.split('@|.com|.org|.net|.edu|.gov', email)
        
        if len(separations) != 3:
            # Checks if the email address has exactly one '@' symbol, one domain, and one tld
            print(f"{email} is not a valid email address, as it should contain exactly one '@' symbol, a domain name, and exactly one top-level domain (.com,etc).\n")

        else:
            local_part, domain, tld = separations #assigns the local part, domain, and tld to separations
            if local_part == "" or domain == "":
                # Checks if the local part or domain is empty
                print(f"{email} is not a valid email address, as it should contain a non-empty local part and a domain name.\n")

            elif tld != "":
                # Ensures that the top-level domain is empty, meaning there is nothing after it
                print(f"{email} is not a valid email address, as it should contain a top-level domain (.com, .org, etc.) with nothing following it.\n")
           
            else:
                return print(f"{email} appears to be a valid email address.\n")
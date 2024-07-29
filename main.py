import random  # Import the random module to generate random values

def generatePassword():
    # Define character sets for password generation
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Uppercase letters
    lower_case = upper_case.lower()  # Lowercase letters
    digits = '0123456789'  # Digits
    special_characters = "~!@#$%^&*()_-+={[}]|:;'<,>.?/"  # Special characters
    all_characters = upper_case + lower_case + digits + special_characters  # Combined character set
    password = ""  # Initialize an empty string to build the password

    # Prompt the user to enter the desired password length
    length = int(input("Enter password length: "))
    
    try:
        # Validate the password length
        if length < 4:
            # Raise an error if the length is less than 4
            raise ValueError("Password length must be at least 4 to include all character types.")
        else:
            # Generate the password
            while len(password) < length:
                # Append a random character from all_characters to the password
                password += all_characters[random.randint(0, len(all_characters)-1)]
                
            # Print the generated password
            print(f"Generated Password:\n{password}")
    except ValueError as e:
        # Print the error message if a ValueError is raised
        print(e)

# Call the generatePassword function to run the password generation
generatePassword()

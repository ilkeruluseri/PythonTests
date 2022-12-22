def task1():  # First question
    invalid_username = True
    while invalid_username:  # Validation loop for username
        username = input("Please enter a username: ")
        invalid_username = username[0] != "e" or len(username) < 6 or len(username) > 12 or not username.isalnum()  # Conditions for username
        if len(username) < 6 or len(username) > 12:
            print("Please enter a username in the allowed length!")
        elif username[0] != "e":
            print("Please use 'e' at the beginning of the username")
        elif not username.isalnum():
            print("Username can only contain alphanumeric characters")
    print("Your username", username, "is VALID")
    invalid_password = True
    while invalid_password:  # Validation loop for password
        password = input("Please enter a password: ")
        invalid_password = len(password) < 8
        if invalid_password:
            print("Password should be at least 8 characters")
    print("You were successfully registered as", username)


def task2():  # Second question
    user_str = input("Write your text! ")
    special_chr = input("Enter which character to search for: ")
    while len(special_chr) != 1:  # To validate that user entered one character
        special_chr = input("You can only enter one character! Enter which character to search for: ")
    special_chr_counter = 0
    for i in user_str:
        if i == special_chr:
            special_chr_counter += 1
    print("We have found", special_chr_counter, "special character", special_chr)


task1()  # Calling first questions code
task2()  # Calling second questions code

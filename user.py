users = [("user1", "1234"), ("user2", "5678")]


def create_user():
    new_username = input("Create Username: ")
    username_exists = False
    for i in users:
        if new_username == i[0]:
            username_exists = True
    if username_exists:
        print("Username already exists")
        create_user()
    else:
        new_password = input("Create Password: ")
        confirm_password = input("Confirm Password: ")
        if new_password == confirm_password:
            users.append((new_username, new_password))
        else:
            print("Passwords aren't the same")
            create_user()
    take_command()
  

def log_in():
    logged_in = False
    username_input = input("Enter Username: ")
    password_input = input("Enter Password: ")
    for i in users:
        if username_input == i[0] and password_input == i[1]:
            print("Logged in as", i[0])
            logged_in = True

    if not logged_in:
        print("Wrong username or password")
        log_in()
    take_command()


def take_command():
    print("Available Commands: \n"
          "log in \n"
          "create user \n"
          "exit")
    command = input("Enter command: ")
    if command == "log in":
        log_in()
    elif command == "create user":
        create_user()
    elif command == "exit":
        print("Exiting...")
    else:
        print("Unknown command")
        take_command()

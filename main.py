import prime_checker
import user
import armstrong
import encryption
import ceng113_hw1_300201033

while True:
    selection = input("Which function would you like to use? \n"
                      "1- Armstrong number checker \n"
                      "2- Armstrong number lister \n"
                      "3- Prime number checker \n"
                      "4- User log in system \n"
                      "5- Card drawer \n"
                      "6- Encryption-Decryption \n"
                      "Press x to exit \n"
                      )
    if selection == "1":
        armstrong.armstrong_number_checker()
    elif selection == "2":
        armstrong.armstrong_lister()
    elif selection == "3":
        prime_checker.prime_checker()
    elif selection == "4":
        user.take_command()
    elif selection == "5":
        ceng113_hw1_300201033.card_drawer()
    elif selection == "6":
        pass
    elif selection == "x":
        print("Exiting...")
        break
    else:
        print("Invalid input")

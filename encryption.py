print("Would you like to encrypt a message or decrypt one?\n"
      "Note: You can only decrypt messages encrypted by this program.\n"
      )

letter_numbers = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
    "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25
}
numbers_letters = {v: k for k, v in letter_numbers.items()}


def text_into_numbers(text):
    number_version = []
    for i in text:
        number_version.append(letter_numbers[i])
    return number_version


def numbers_into_text(numbers):
    text_version = []
    for i in numbers:
        text_version.append(numbers_letters[i])
    return text_version


def encrypt(x):
    new_list = []
    iteration = 0
    for i in x:
        iteration += 1
        if iteration % 2 == 0:
            new_list.append((i + 3) % 26)
        else:
            new_list.append((i - 3) % 26)
    new_list = numbers_into_text(new_list)
    return new_list


def decrypt(x):
    x = text_into_numbers(x)
    new_list = []
    iteration = 0
    for i in x:
        iteration += 1
        if iteration % 2 == 0:
            new_list.append((i - 3) % 26)
        else:
            new_list.append((i + 3) % 26)
    new_list = numbers_into_text(new_list)
    return new_list


"""
encrypted_text = encrypt(text_into_numbers(text_input))
print("Encrpyted text: ", end="")
for i in encrypted_text:
    print(i, end="")

decrypted_text = decrypt(encrypted_text)
print("\nDecrypted text: ", end="")
for i in decrypted_text:
    print(i, end="")
"""
user_choice = input("1-Encrypt\n"  
                    "2-Decrypt\n")
if user_choice == "1":
    text_input = input("Enter text: ")
    encrypted_text = encrypt(text_into_numbers(text_input))
    print("Encrpyted text: ", end="")
    for i in encrypted_text:
        print(i, end="")
elif user_choice == "2":
    text_input = input("Enter text: ")
    decrypted_text = decrypt(text_input)
    print("\nDecrypted text: ", end="")
    for i in decrypted_text:
        print(i, end="")

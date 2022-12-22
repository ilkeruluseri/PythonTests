def binary_to_decimal():
    binary_input = int(input("Enter binary "))
    length = len(str(binary_input))
    result = 0
    count = 0
    for i in str(binary_input):
        count += 1
        result += 2**(length - count)*int(i)
    print(result)


def decimal_to_binary():
    decimal_input = int(input("Enter decimal "))
    x = decimal_input
    result = ""
    while x > 0:
        if x % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        x = x//2
    print(result)



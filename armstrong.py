def armstrong_number_checker():
    num = int(input("num: "))
    divider = 10
    new_divider = divider
    num_length = 0
    num_checker = num

    total_sum = 0
    num_length = len(str(num))
    # print(num_length)
    power = 0
    while num_checker != 0:
        a = num_checker % divider
        num_checker -= a
        #  print(a // (divider / 10))
        power = (a // (divider / 10)) ** num_length
        #   print(power)
        total_sum += power
        divider *= 10

    if total_sum == num:
        print(num, "is an armstrong number")
    else:
        print(num, "is not an armstrong number")

def armstrong_lister():
    limit = int(input("Enter limit: "))
    for i in range(1, limit+1):
        num = i

        divider = 10
        new_divider = divider
        num_length = 0
        num_checker = num

        total_sum = 0
        num_length = len(str(num))
        # print(num_length)
        power = 0
        while num_checker != 0:
            a = num_checker % divider
            num_checker -= a
            #  print(a // (divider / 10))
            power = (a // (divider / 10)) ** num_length
            #   print(power)
            total_sum += power
            divider *= 10

        if total_sum == num:
            print(num, "is an armstrong number")




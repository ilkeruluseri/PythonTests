def prime_checker():
    num = int(input("Number: "))
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime:
        print(num, "is prime.")
    else:
        print(num, "is not prime")
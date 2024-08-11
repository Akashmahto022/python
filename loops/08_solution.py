number = 23
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("that is not a prime number")
            break
        else:
            print(number, "is a prime number")
            break

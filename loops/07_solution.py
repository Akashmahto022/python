
while True:
    number = int(input("guess the number"))
    if 1 <= number <= 10:
        print("you got this")
        break
    else:
        print("invalid number! try again")
        continue
    
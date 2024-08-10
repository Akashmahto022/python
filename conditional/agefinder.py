age = int(input("Enter your age in number"))

if age < 13:
    print("Child")
elif age < 18:
    print("teenager")
elif age > 18:
    print("adult")
elif age > 60:
    print("senior")
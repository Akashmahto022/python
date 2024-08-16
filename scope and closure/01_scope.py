# username = "Akash"

# def name():
#     # username = "mahto"
#     print(username)
    
# print(username)
# name()


def f1():
    x = 88
    def f2():
        print(x)
    return f2

result = f1()
result()


def number(num):
    def actual(x):
        return x ** num
    return actual

f = number(2)
g = number(3)

print(f(3))
print(g(3))
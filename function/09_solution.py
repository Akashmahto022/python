# yield function

def evennumber(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in evennumber(10):
    print(num)


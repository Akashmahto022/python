import math

def  areaOfCircle(radius):
    area = math.floor((math.pi * radius ** 2)*100)/100
    circumfrance = math.floor((2 * math.pi * radius)*100)/100
    return area, circumfrance

a,c = areaOfCircle(3)

print(a, c)
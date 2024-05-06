import types

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

def calculateArea(self):
    return self.base*self.height/2.0

t1 = Triangle(4.0, 5.0)
t1.calculateArea = types.MethodType(calculateArea, t1)

print(t1.calculateArea())
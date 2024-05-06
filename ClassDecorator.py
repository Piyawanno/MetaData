import math

def setPostProcess(postprocess):
    def decorate(klass):
        if issubclass(klass, Shape) :
            calculateCircumstance = klass.calculateCircumstance
            calculateArea = klass.calculateArea
            def postCircumstance(self):
                result = calculateCircumstance(self)
                return postprocess(result)
            def postArea(self):
                result = calculateArea(self)
                return postprocess(result)
            klass.calculateCircumstance = postCircumstance
            klass.calculateArea = postArea
        return klass
    return decorate

def double(x):
    return x*2

def triple(x):
    return x*3

class Shape:
    def calculateCircumstance(self):
        raise NotImplementedError
    
    def calculateArea(self):
        raise NotImplementedError

@setPostProcess(double)
class Circle (Shape):
    def __init__(self, r):
        self.r = r

    def calculateCircumstance(self):
        return math.pi*self.r*2
    
    def calculateArea(self):
        return math.pi*self.r**2

@setPostProcess(triple)
class Rectangle (Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculateCircumstance(self):
        return self.width*2 + self.length*2
    
    def calculateArea(self):
        return self.width*self.length


c1 = Circle(2.0)
print(c1.calculateCircumstance())
print(c1.calculateArea())

r1 = Rectangle(2.0, 4.0)
print(r1.calculateCircumstance())
print(r1.calculateArea())

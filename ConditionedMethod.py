def prepareMethod(isOdd):
    def prepare(klass):
        def calculateOdd(self):
            return (self.x+1)/2
        def calculateEven(self):
            return self.x/2
        if isOdd:
            klass.calculate = calculateOdd
        else:
            klass.calculate = calculateEven
        return klass
    return prepare

@prepareMethod(False)
class Calculator:
    def __init__(self, x):
        self.x = x

c = Calculator(6.0)
print(c.calculate())
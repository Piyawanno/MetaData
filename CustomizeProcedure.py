def standardProcedure(callable):
    def wrapper(x):
        y = x**2
        z = callable(y)
        return z/2.0
    return wrapper

@standardProcedure
def addFive(x):
    return x+5

print(addFive(2))

def addSix(x):
    return x+6

procedure = standardProcedure(addSix)
print(procedure(3))

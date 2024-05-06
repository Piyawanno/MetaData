def setAsPolynomial(callable):
    def calculate(x):
        a, b, c = callable.coefficient
        result = a*x**2 + b*x + c
        return callable(result)
    return calculate

def setCoefficient(a, b, c):
    def wrap(callable):
        callable.coefficient = (a, b, c)
        return callable
    return wrap

@setAsPolynomial
@setCoefficient(1.0, 2.0, 1.0)
def double(x):
    return 2*x

print(double(2.0))


def triple(x):
    return 3*x

tripleWithCoefficient = setCoefficient(1.0, 2.0, 1.0)(triple)
triplePolynomial = setAsPolynomial(tripleWithCoefficient)

print(triplePolynomial(3.0))


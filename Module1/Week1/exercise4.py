import math

def sin_approx(x, terms=10):
    sin_x = 0
    for n in range(terms):
        term = ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n+1)
        sin_x += term
    return sin_x

def cos_approx(x, terms=10):
    cos_x = 0
    for n in range(terms):
        term = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
        cos_x += term
    return cos_x

def sinh_approx(x, terms=10):

    sinh_x = 0
    for n in range(terms):
        term = (x**(2*n+1)) / math.factorial(2*n+1)
        sinh_x += term
    return sinh_x

def cosh_approx(x, terms=10):

    cosh_x = 0
    for n in range(terms):
        term = (x**(2*n)) / math.factorial(2*n)
        cosh_x += term
    return cosh_x

terms = 10
x = 3.14

print(f"sin(x={x}, n= {terms}) ≈ {sin_approx(x, terms)}")
print(f"cos(x={x}, n= {terms}) ≈ {cos_approx(x, terms)}")
print(f"sinh(x={x}, n= {terms}) ≈ {sinh_approx(x, terms)}")
print(f"cosh(x={x}, n= {terms}) ≈ {cosh_approx(x, terms)}")
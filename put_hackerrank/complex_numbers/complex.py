import cmath
expr = input()
[a, b] = expr.strip().split("+")
b = b[:-1]
a, b = int(a), int(b)
modulus, argument = cmath.polar(complex(a, b))
print(modulus)
print(argument)

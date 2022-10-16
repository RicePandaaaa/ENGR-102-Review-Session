print(type(5/5))

"""
Types

Addition, Subtraction, Multiplication, Exponent
a + b, a - b, a * b, a ** b

if a and b are both ints, the result will be an int
if either a or b is a float, the result will be a float

Division:
 - Modulus (%)
 - 'Standard' (/)
 - Integer (//)

Standard always gives you a float. Integer and modulus obey rules as +/-/*/**
"""

print(type(1 + 1), type(1 - 1), type(1 * 1), type(1 ** 1))
print(type(1.0 + 1), type(1.0 - 1), type(1.0 * 1), type(1 ** 1.0))

print(type(1 / 1), type(1 // 1), type(1 % 1))
print(type(1.0 / 1), type(1 // 1.0), type(1 % 1.0))
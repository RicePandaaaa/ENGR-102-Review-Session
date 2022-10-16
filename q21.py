# For checking reasons
import math

# Take in x
x = float(input("Enter x: "))

while not (-1 < x < 1):
    x = float(input("Enter x: "))

# Counter variables
approximation = 0
exponent = 1

# Loop and add
while abs((2 / exponent) * (x ** exponent)) >= 10 ** -6:
    approximation += (2 / exponent) * (x ** exponent)
    exponent += 2

# Output
print(approximation)
# For checking reasons
print(math.log((1 + x) / (1 - x)))
print((2 / exponent) * (x ** exponent))
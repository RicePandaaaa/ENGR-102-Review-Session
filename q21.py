# For checking reasons
import math

# Take in x
x = float(input("Enter x: "))

# Counter variables
approximation = 2 * x
exponent = 3

# Loop
while (2 / exponent) * (x ** exponent) >= 10.0**-6:
    approximation += (2 / exponent) * (x ** exponent)
    exponent += 2

# Output
print(approximation)
# For checking reasons
print(math.log((1 + x) / (1 - x)))
print((2 / exponent) * (x ** exponent))
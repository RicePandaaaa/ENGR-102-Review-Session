"""
Important notes:
 - Tolerance is 10 ^ -6
"""

# Take in x
x = float(input("Please enter x: "))

# Counter variables
approximation = 1
exponent = 1

# Loop
while abs(x ** exponent) >= 10**-6:
    approximation += x ** exponent
    exponent += 1

# Output
print(approximation)
# For checking purposes
print(1 / (1 - x))
print(x ** exponent)
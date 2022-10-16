"""
Write Python code which asks for input of a value of x on the interval -1 < x < 1, and which computes an
approximation to 1/(1-x) using the using the series expansion summation. The summation should be
continued until the term to be added to the summation is less than 10-6 in absolute value. Hint: Note that
each term in the series is x raised to a power, including the 1 and x terms: x0=1 and x1=x
"""

# Take in x
x = float(input("Please enter x: "))

# Plug in x to the summation
approximation = 1
exponent = 1

# Loop
while abs(x ** exponent) >= 10**-6:
    approximation += x ** exponent
    exponent += 1

# Output and check answer
print(approximation)
print(1 / (1 - x))
print(x ** exponent)
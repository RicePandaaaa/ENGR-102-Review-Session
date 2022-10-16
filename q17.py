"""
Given a list xdata of unknown length that contains x values, write the code to calculate a y-value for each
x-value using the equation below. Store the calculated y values in a list called y_data. Do not use numpy
arrays for this problem. Please use Python list functions, list methods, and list operators.

y = 4.12x**2 + 1.52x - 7.1
"""

# Data sets
xdata = [-1, 0, 1]
y_data = []

# Plug in 
for x in xdata:
    y = (4.12 * (x ** 2)) + (1.52 * x) - 7.1
    y_data.append(y)

# For the sake of checking our results...
print(y_data)

"""
Without using a list, array, or tuple, write the Python code that will input a series of positive floating point
numbers until a negative value is entered. The program should then output the maximum number, the
minimum number and the average number for this series.
"""

# Store the data
maximum_number = "N/A"
minimum_number = "N/A"
total = "N/A"
count = 0

# Get first input
number = int(input("Enter a number: "))

# Looping and updating
while number > 0:
    # Update for the first number
    if count == 0:
        maximum_number = number
        minimum_number = number
        total = number
        count = 1

    # Update for every number past the first one
    else:
        if number > maximum_number:
            maximum_number = number
        if number < minimum_number:
            minimum_number = number
        total += number
        count += 1

    # Ask for another number
    number = int(input("Enter a number: "))

# Calculate the average
average = "N/A"

# If a numeric average is possible, then make one
if count > 0:
    average = total / count

# Output
print(f"Max: {maximum_number}, Min: {minimum_number}, Average: {average}")

"""
Ternary Operator (?:)

Usually for an if-else, it looks like this

var = ""
if condition 1 is true:
    var = value when true
else:
    var = value when false

With the ternary operator:
var = (condition 1) ? (value if true) : (value if false)

In python, it's slightly different
var = (value if true) if (condition 1) else (value if false)

status = "EVEN" if (x % 2 == 0) else "ODD"
print(status)

status = ""
if x % 2 == 0:
    status = "EVEN"
else:
    status = "ODD"
"""
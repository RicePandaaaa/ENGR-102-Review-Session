"""
Without using a list, array, or tuple, write the Python code that will input a series of positive floating point
numbers until a negative value is entered. The program should then output the maximum number, the
minimum number and the average number for this series.
"""

# Data values to store
maximum = "N/A"
minimum = "N/A"
total = "N/A"
count = 0

# Take input
number = float(input("Enter a number: "))

# Loop
while number > 0:
    # Update variables to first number
    if count == 0:
        maximum = number
        minimum = number
        total = number
        count += 1
    
    # Update variables based on non first number
    else:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
        total += number
        count += 1

    # Ask for next number
    number = float(input("Enter a number: "))

# Safeguard against having 0 numbers
average = "N/A"
if count > 0:
    average = total / count

# Output
print(f"Max: {maximum}, Min: {minimum}, Average: {average}")


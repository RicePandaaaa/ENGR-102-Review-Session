"""
Write a Python program that takes as inputs 5 integers. The program should check to see if any of the 5 are
duplicates of another (i.e., check whether any of the integers were entered more than once). If, after all inputs
are entered, a duplicate is found, the program should print "Duplicates", otherwise it should print "All Unique".
"""

# Store the input
numbers = []

# Take in the input
# for i in range(5):
while len(numbers) < 5:
    number = int(input("Enter a number: "))
    numbers.append(number)

# Flag to check for duplicates
duplicates_found = False

# Nested for loop to check each number against the others
# First for loop will grab a number
for i in range(0, 5):
    # Second for loop will check numbers[i] against all the other numbers
    for j in range(0, 5):
        if numbers[i] == numbers[j] and i != j:
            duplicates_found = True

# Output
if duplicates_found:
    print("Duplicates")
else:
    print("All Unique")

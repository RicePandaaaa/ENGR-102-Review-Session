"""
Write a Python program that takes as inputs 5 integers. The program should check to see if any of the 5 are
duplicates of another (i.e., check whether any of the integers were entered more than once). If, after all inputs
are entered, a duplicate is found, the program should print "Duplicates", otherwise it should print "All Unique".
"""

# Storage
numbers = []

# Loop and take input
while len(numbers) < 5:
    number = int(input("Enter a number: "))
    numbers.append(number)

    """
    alternate solution, add this for loop instead of having the nested for loop outside

    for n in numbers:
        if n == number:
            duplicate has been found

    # Dont forget to flag appropriately
    """

# Flag for duplicates
duplicates_found = False

# Duplication check
# Take each number in the list and compare it to the other four

# First for loop, grab the number
for i in range(len(numbers)):
    # Second for loop, go through all the other numbers
    for j in range(len(numbers)):
        # Check for duplicate
        if numbers[i] == numbers[j] and i != j:
            duplicates_found = True

# Output
if duplicates_found:
    print("Duplicates")
else:
    print("All Unique")

"""
[1, 2, 1]

i = 0, j = 2
i is not equal to j

1 == 1 true, are duplicates because they're in different locations
"""
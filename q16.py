"""
Write a Python program which uses loops that can output the following pattern.
1
22
333
4444
55555
666666
7777777
88888888
"""

# First for loop will go from 1 to 8
for i in range(1, 9):
    # Second for loop will output i i times
    for j in range(i):
        print(i, end="")
    # Line buffer
    print()

# Alternate solution
for i in range(1, 9):
    print(str(i) * i)
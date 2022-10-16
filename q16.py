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

"""
String multiplication

"a" * 3 = "a" + "a" + "a" = "aaa"
"""

# Loop and print
for i in range(1, 9):
    print(str(i) * i)

# Nested for loop version
# First loop will grab the number and place it in i
for i in range(1, 9):
    # Second loop will output the number i times
    for j in range(i):
        print(i, end="")
    print()


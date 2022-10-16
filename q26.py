"""
If we have a list called L of length > 10, using list slicing create a sub list called L_new of the 4th through the
7th elements of L. Now show how to modify the list L by removing the 2nd, 3rd, and 4th elements.
"""

# Make a list L with 11 elements (len(L) > 10)
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sublist
L_new = L[3:7]
print(L_new)

# Removal (wrong)
# Expected L: [0, 4, 5, 6, 7, 8, 9, 10]
"""
for i in range(1, 4):
    del L[i]
    print(L)

also wrong
del L[1]
del L[2]
del L[3]
"""

"""
# Removal (correct, in place deletion)
for i in range(3):
    del L[1]
"""
"""
# Backwards removal
for i in range(3, 0, -1):
    del L[i]

or this (same thing)
del L[3]
del L[2]
del L[1]
"""

# Slicing
L = L[0:1] + L[4:]

# Output to check
print(L)
"""
When you remove an element from a list, everything to its right shifts to the left by one index
"""
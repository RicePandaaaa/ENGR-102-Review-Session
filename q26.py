"""
If we have a list called L of length > 10, using list slicing create a sub list called L_new of the 4th through the
7th elements of L. Now show how to modify the list L by removing the 2nd, 3rd, and 4th elements.

I assume the first element is at index 0.
"""

# Make a list L with 11 elements (len(L) > 10)
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make L_new
L_new = L[3:7]

# Removing the values
# Easy way with slicing
L = L[0:1] + L[4:]
print(L)


# Literally just deleting one by one
"""
# Wrong way
L.pop(1)
L.pop(2)
L.pop(3)

# Alternate correct way, in place removal
for i in range(3):
    L.pop(1)

print(L)

# Alternate correct way, backwards removal
for i in range(3, 0, -1):
    L.pop(i)

print(L)

When you remove from a list, every item to the removed item's right shifts over to the left by 1
"""
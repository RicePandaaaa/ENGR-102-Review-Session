x = 3
y = 5

print(x != y - 2)
print(x >= 0 and (not x < 10))
print(x < 0 and x < 10)
print(x >= 0 and x < 2)
print(x < 0 or y > 5)
print((not x > 0) or x < 10)

"""
Short circuiting, not checking all the conditions

and:

condition 1 and condition 2
if condition 1 is false, the whole and expression is false, and condition 2 is never checked

l = [1, 2, 3]

if len(l) > 3 and l[3] == 4:
    print("HI")
else:
    print("BYE")

if len(l) > 3:
    print("TONY")
    if l[3] == 4:
        print("HI")
    else:
        print("BYE")
else:
    print("BYE")

or:
condition 1 or condition 2
same thing, if the first condition is true, the whole or statement is true, and the second condition is ignored
"""
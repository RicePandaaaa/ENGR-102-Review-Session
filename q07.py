a = 1
b = 2
c = 'a'
d = int(float('3.14'))  # 3
if a == 1 and d == 3.14:
    print('Green')
elif c == a or d > 3:
    print('Red')
else:
    print('Yellow')

"""
Short ciruiting crash course

and - both conditions must be true
condition 1 and condition 2

if condition 1 is false, we never condition 2

l = [1, 2, 3]

if len(l) > 3 and l[3] == 4:
    print("HI")
else:
    print("BYE")

if len(l) > 3:
    if l[3] == 4:
        print("HI")
    else:
        print("BYE")
else:
    print("BYE")

or - either condition needs to be true for it to be true
condition 1 or condition 2

if condition 1 is true, then we never check condition 2

l = [1, 2, 3]

if l[0] == 1 or l[4] == 5:
    print("HI")
"""

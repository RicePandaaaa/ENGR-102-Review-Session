x = 2
y = "A"
while x<100:
    print(x, y)
    x *= x      # 2 -> 4 -> 16 -> 256
    y += y      # A -> AA -> AAAA -> AAAAAAAA
print(x)
print(y)
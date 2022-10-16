num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
numSum = num1 + num2

if numSum < 0:
    myString = str(-numSum)
else:
    myString = str(numSum)
strLength = len(myString)
print('number of digits of ', numSum,'is ', strLength)


"""
temp = 123

123 / 10 = 12.3
12 / 10 = 1.2
1 / 10 = 0.1
"""
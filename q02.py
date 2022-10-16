num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
numSum = num1 + num2

# answers go down here
if numSum < 0:
    myString = str(numSum)
else:
    myString = str(numSum)
strLength = len(myString)
print('number of digits of ', numSum,'is ', strLength)

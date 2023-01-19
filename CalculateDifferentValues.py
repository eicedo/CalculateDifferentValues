num1 = float(input('Enter a floating-point value: \n'))
num2 = float(input('Enter a floating-point value: \n'))
num3 = float(input('Enter a floating-point value: \n'))
num4 = float(input('Enter a floating-point value: \n'))
num5 = float(input('Enter a floating-point value: \n'))

values = [num1, num2, num3, num4, num5]
 
sumOfNums = 0
count = 0
minimum = values[0]
maximum = values[0]
interestList =[]
for num in values:
    sumOfNums += num #adding the num value to sumOFNums
    count += 1       #count of elements in values[]
average = sumOfNums / count

if minimum > num:
    minimum = num

elif maximum < num:
    maximum = num

interestList = [num + num * .2 for num in values] #Created a new list with formula to find interest value


print('Total Value: %d' % sumOfNums)
print('Average Value: %d' % average)
print('Minimum Value: %d' % minimum)
print('Maximum Value: %d' % maximum)
print('Interest at 20 percent for each original value entered:', interestList)
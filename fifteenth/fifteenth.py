squaresSum = 0
for number in range(1,101):
    newNumber = number ** 2
    squaresSum += newNumber


sumSquares = 0
for number in range(1,101):
    sumSquares += number
lastSum = sumSquares**2

print(lastSum-squaresSum)

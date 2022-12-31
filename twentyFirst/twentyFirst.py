def fac(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return(fact)

myNumber = str(fac(100))
sum = 0
for number in myNumber:
    sum += int(number)
print(sum)

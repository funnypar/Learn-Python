def isPrime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i == 0:
            return False
            break
    return True

sum = 0
for j in range(2,2000001):
    if isPrime(j) == True:
        sum += j
print(sum)

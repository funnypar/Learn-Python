def isPrime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i == 0:
            return False
            break
    return True
myList =[]
for j in range(2,150000):
    if isPrime(j) == True:
        myList.append(j)
        if len(myList) == 10001:
            print(myList[-1])
            break

# This was not a good way , I just want to solve the problem 😂😂😂

def isPrime(number):
    numbers = range(2,int(number**0.5)+1)
    for numb in numbers:
        if number % numb == 0 :
            return False
            break
    return True

def findFactor(number):
    numbers = range(2,int(number/2)+1)
    for numb in numbers:
        if number % numb == 0 and isPrime(numb):
            print(numb)

findFactor(600851475143)

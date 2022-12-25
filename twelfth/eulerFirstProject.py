numbersList = list()
for number in range(1,1000):
    if number%5 == 0 or number%3==0:
        numbersList.append(number)
print(sum(numbersList))

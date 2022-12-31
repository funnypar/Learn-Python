with open('data.txt', 'r') as file:
    sum = 0
    for number in file:
        sum += int(number)
    print(str(sum)[:10])

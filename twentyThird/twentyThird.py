numbers = {
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety",
100: "onehundred",
200: "twohundred",
300: "threehundred",
400: "fourhundred",
500: "fivehundred",
600: "sixhundred",
700: "sevenhundred",
800: "eighthundred",
900: "ninehundred",
1000: "onethousand"
}

# create 21 - 99
for number in range(20,29):
    numbers[number+1] = "twenty"+ numbers.get(list(numbers.keys())[number-20])
for number in range(30,39):
    numbers[number+1] = "thirty"+ numbers.get(list(numbers.keys())[number-30])
for number in range(40,49):
    numbers[number+1] = "forty"+ numbers.get(list(numbers.keys())[number-40])
for number in range(50,59):
    numbers[number+1] = "fifty"+ numbers.get(list(numbers.keys())[number-50])
for number in range(60,69):
    numbers[number+1] = "sixty"+ numbers.get(list(numbers.keys())[number-60])
for number in range(70,79):
    numbers[number+1] = "seventy"+ numbers.get(list(numbers.keys())[number-70])
for number in range(80,89):
    numbers[number+1] = "eighty"+ numbers.get(list(numbers.keys())[number-80])
for number in range(90,99):
    numbers[number+1] = "ninety"+ numbers.get(list(numbers.keys())[number-90])

# create 101-999
for number in range (100,199):
    numbers[number+1] = "onehundredand"+ numbers.get(number-99)
for number in range (200,299):
    numbers[number+1] = "twohundredand"+ numbers.get(number-199)
for number in range (300,399):
    numbers[number+1] = "threehundredand"+ numbers.get(number-299)
for number in range (400,499):
    numbers[number+1] = "fourhundredand"+ numbers.get(number-399)
for number in range (500,599):
    numbers[number+1] = "fivehundredand"+ numbers.get(number-499)
for number in range (600,699):
    numbers[number+1] = "sixhundredand"+ numbers.get(number-599)
for number in range (700,799):
    numbers[number+1] = "sevenhundredand"+ numbers.get(number-699)
for number in range (800,899):
    numbers[number+1] = "eighthundredand"+ numbers.get(number-799)
for number in range (900,999):
    numbers[number+1] = "ninehundredand"+ numbers.get(number-899)

# sort the dict
newnumbers = dict(sorted(numbers.items()))

# calculate letters
sum = 0
for i in range(0,1000):
    sum += len(list(newnumbers.values())[i])
print("The answer is :   " + sum)

print("\n------------------------------------------- Prime Number ✏️ --------------------------------------------\n\n")
userNumber= int(input("Enter your number :    "))
status = True
for number in range(2,userNumber):
    if userNumber % number == 0 :
        status = False
        print("For this number is not prime !", number)
if status == True :
        print("\nThis number is prime !\n\n")

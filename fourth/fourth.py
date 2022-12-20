count = 0;
sum = 0;
print("\n\n\n\n---------------------------------------------------- Average ----------------------------------------------------")
userNumber = input("\n\nPlease enter your numbers 😊 : (💥if you want no more number => enter : -1)\n\n");
while int(userNumber) != -1 :
    count += 1 ;
    sum = sum + int(userNumber);
    userNumber = input("\nPlease enter your numbers ❤️ : (💥if you want no more number => enter : -1)\n\n");
average = sum/count;
print ("\n\n\n💻The average of your numbers is 😁 :     ", average,"\n\n\n\n\n")

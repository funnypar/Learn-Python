import random

#Mopano function ***************************************************************
def game(name):
    pcAnswer = random.randint(1,99)
    print("Okay ",name, " Let's Goooooo!!!!\n\n")
    userAnswer = int(input("Please Enter your guess ๐ฝ:  \n"))
    i = 5
    while userAnswer != pcAnswer and i > 1 :
        if pcAnswer > userAnswer:
            print("mine is higher ๐")
            i -=1
            userAnswer = int(input("\n\nPlease Enter your guess again ๐:  \n"))
        elif pcAnswer < userAnswer:
            print("mine is smaller ๐คฆโโ๏ธ")
            i -=1
            userAnswer = int(input("\n\nPlease Enter your guess again ๐:  \n"))
    if pcAnswer == userAnswer:
        print(name, "  Woooowwwww! you did that ๐ฅโค๏ธ๐")
    else:
        print("You are a loserrrrrrrrr ๐๐๐" , name)


#Start Game ********************************************************************

print("------------------------------------------ Guess game ๐ฎ -----------------------------------------------")
LikeToPaly = input("Would you like to play ? (yes๐ : y  ,  no ๐ : n)\n\n")
if LikeToPaly == "y" :
    name = input("\nWhat is your name ? \n\n")
    game(name)
    playAgain = input("\nWould you like to play again ? ๐ (yes๐ : y  ,  no ๐ : n)\n\n")
    while playAgain == "y":
        game(name)
        playAgain = input("\nWould you like to play again ? ๐ (yes๐ : y  ,  no ๐ : n)\n\n")
    print("\n\nYou are a loserrrrrrrrr ๐๐๐" , name)
else:
    print("\n\nOkey loser ๐ต๐คช")

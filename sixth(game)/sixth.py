import random

#Mopano function ***************************************************************
def game(name):
    pcAnswer = random.randint(1,99)
    print("Okay ",name, " Let's Goooooo!!!!\n\n")
    userAnswer = int(input("Please Enter your guess 👽:  \n"))
    i = 5
    while userAnswer != pcAnswer and i > 1 :
        if pcAnswer > userAnswer:
            print("mine is higher 😈")
            i -=1
            userAnswer = int(input("\n\nPlease Enter your guess again 😁:  \n"))
        elif pcAnswer < userAnswer:
            print("mine is smaller 🤦‍♂️")
            i -=1
            userAnswer = int(input("\n\nPlease Enter your guess again 😁:  \n"))
    if pcAnswer == userAnswer:
        print(name, "  Woooowwwww! you did that 💥❤️😍")
    else:
        print("You are a loserrrrrrrrr 😈😈😈" , name)


#Start Game ********************************************************************

print("------------------------------------------ Guess game 🎮 -----------------------------------------------")
LikeToPaly = input("Would you like to play ? (yes😊 : y  ,  no 😒 : n)\n\n")
if LikeToPaly == "y" :
    name = input("\nWhat is your name ? \n\n")
    game(name)
    playAgain = input("\nWould you like to play again ? 😊 (yes😊 : y  ,  no 😒 : n)\n\n")
    while playAgain == "y":
        game(name)
        playAgain = input("\nWould you like to play again ? 😊 (yes😊 : y  ,  no 😒 : n)\n\n")
    print("\n\nYou are a loserrrrrrrrr 😈😈😈" , name)
else:
    print("\n\nOkey loser 😵🤪")

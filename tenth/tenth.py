import csv
from statistics import mean
# ---------------------------------------- Functions ------------------------------------------
def heighest(dict):
    maxScore = max(sorted(dict.items(), key=lambda item:item[1]))
    print("%s has a heighest average 🤓 :  %5.2f " %(maxScore[0], maxScore[1]))

def lowest(dict):
    minScore = min(sorted(dict.items(), key=lambda item:item[1]))
    print("%s has a lowest average 🤓 :  %5.2f " %(minScore[0], minScore[1]))
# ----------------------------------------- Programm ------------------------------------------
print("\n\n------------------------------------- Average of class 👽 -------------------------------------------\n")
teacherInput = input("Hi 😁 do you want to see all of the average ? (y : yes🥸 , n : no😒 )\n")
if teacherInput == "y":
    with open("studentsScores.csv") as studentsScores:
        reader = csv.reader(studentsScores)
        scoresDict = dict()
        for row in reader:
            name = row[0]
            scores = row[1:]
            fScores = list()
            for score in scores:
                fScores.append(float(score))
                scoresDict[name] = mean(fScores)
            print("\n%s average is : %5.2f " % (name ,mean(fScores)))
    teacherInput_1 = input("\n\ndo you want to know who has the highest or lowest average ? (h : heighest🤓 , l : lowest☠️ n: no😒 )\n")
    while  teacherInput_1 != "n":
        if teacherInput_1 == "h":
            heighest(scoresDict)
            teacherInput_1 = input("\ndo you want to know who has the highest or lowest average ? (h : heighest🤓 , l : lowest☠️ n: no😒 )\n")
        elif teacherInput_1 == "l":
            lowest(scoresDict)
            teacherInput_1 = input("\ndo you want to know who has the highest or lowest average ? (h : heighest🤓 , l : lowest☠️ n: no😒 )\n")
    print("\n\nbye teacher 😍\n")
else:
    print("\n\nbye teacher 😍\n")

from statistics import mean

fin = open("scores.txt")

listOfScores = []
for line in fin :
    listOfScores.append(float(line.strip()))
print("Your class average is  :  %s " % mean(listOfScores))

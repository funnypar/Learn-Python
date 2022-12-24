import csv
import hashlib

numbers = range(0,10000)
hashDict= dict()
for number in numbers:
    numHash = hashlib.sha256(bytes(str(number),encoding='utf-8')).hexdigest()
    hashDict[numHash]= number
for hash in list(hashDict.keys()):
    with open("userPassword.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            userHash = row[1]
            if userHash == hash :
               status = True
               print("password☠️ of %s is : %s " % (name , hashDict[hash]))
               break

# Get the string from the user
string = input("\nPlease write your string: \n --> ")
# Variables
dic = {}
words = [*string.replace(' ','')]
# create dict to have all words
for word in words :
    if word in dic :
        dic[word] += 1
    else :
        dic[word] = 0
# find the numbers of one char
largest = sorted([*dic.values()]).pop()
# Find the key of char 
def find_key (dic,val):
    for key, value in dic.items():
        if value == val:
            return key
#  Print the result
print(f"\nThe char is --> {find_key(dic,largest)}\n")


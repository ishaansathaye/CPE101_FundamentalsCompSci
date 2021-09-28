import random

names = ["ada lovelace", "grace hopper", "barbara liskov"]

for i in range(len(names)):
    names[i] = names[i].replace(" ", "")

randomLettersList = []

for j in range(len(names)):
    stringHolder = ""
    for k in range(0, 5):
        rand_number = random.randint(0, (len(names[j])-1))
        rand_letter = names[j][rand_number]
        stringHolder = stringHolder + rand_letter
    randomLettersList.append(stringHolder)


print()
for z in range(len(randomLettersList)):
    print(randomLettersList[z] + "@calpoly.edu")
print()
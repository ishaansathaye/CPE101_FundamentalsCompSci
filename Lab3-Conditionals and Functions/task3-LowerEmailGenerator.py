import random

names = []
print()
position = ""
for i in range(0,3):
    if i == 0:
      position = "first"
    elif i == 1:
      position = "second"
    else:
      position = "third"
    # prompt = "Enter the", position, "name (first, last): "
    nameInput = input("Enter the " + position + " name (first, last): ")
    names.append(nameInput)
 
for i in range(len(names)):
    names[i] = names[i].replace(" ", "")
    names[i] = names[i].lower()

#Does not use the same letter chosen (Still Duplicates)
def generateEmails(nameList):
  randomLettersList = []
  listGenerator = ""
  for j in range(len(nameList)):
    stringHolder = ""
    listGenerator = list(nameList[j])
    for k in range(0, 5):
      rand_number = random.randint(0, (len(listGenerator)-1))
      rand_letter = listGenerator[rand_number]
      listGenerator.remove(listGenerator[rand_number])
      stringHolder = stringHolder + rand_letter
    randomLettersList.append(stringHolder)
  return randomLettersList

def displayEmails(randomList):
  print()
  for z in range(len(randomList)):
    print(randomList[z] + "@calpoly.edu")
  print()

displayEmails(generateEmails(names))
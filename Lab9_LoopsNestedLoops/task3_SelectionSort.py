listOfNum = [123, 3, 546, 829, 90, 15, 93]

for i in range(len(listOfNum)):
    min = i
    for j in range(i+1, len(listOfNum)):
        if listOfNum[j] < listOfNum[i]:
            min = j
    listOfNum[i], listOfNum[min] = listOfNum[min], listOfNum[i]

print()
print(listOfNum)
print()
    

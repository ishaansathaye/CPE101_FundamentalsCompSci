list_den = [2, 3, 4, 0, 5, 6, 8]
list_num = []

while len(list_num) != len(list_den):
    print()
    num = input("Enter a number: ")
    if int(num) < 10:
        print("Error!")
    else:
        list_num.append(int(num))

result = []
for i in range(0, 7):
    if list_den[i] == 0:
        result.append(-1)
    else:
        result.append(round((list_num[i]/list_den[i]), 2))

print()
print("Result List: " + str(result))
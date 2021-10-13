from task2_EvenModule import is_even

print()
inputNumber = int(input("Enter a number: "))
evenOrOdd = is_even(inputNumber)

if (evenOrOdd == True) and (inputNumber >= 0):
    print(inputNumber, "is positive and even!")
elif (evenOrOdd == True) and (inputNumber < 0):
    print(inputNumber, "is negative and even!")
elif (evenOrOdd == False) and (inputNumber >= 0):
    print(inputNumber, "is positive and odd!")
elif (evenOrOdd == False) and (inputNumber < 0):
    print(inputNumber, "is negative and odd!")
print()


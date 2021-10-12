def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print()
firstNum = input("Enter the first integer number: ")
operator = input("Enter the operator: ")
secondNum = input("Enter the second integer number: ")

if (operator == '+' or '-' or '*' or '/') and (firstNum.isalpha() == False) and (secondNum.isalpha() == False):
    intFirstNum = int(firstNum)
    intSecNum = int(secondNum)
    if operator == '+':
        print(add(intFirstNum, intSecNum))
    if operator == '-':
        print(subtract(intFirstNum, intSecNum))
    if operator == '*':
        print(mult(intFirstNum, intSecNum))
    if operator == '/':
        print(div(intFirstNum, intSecNum))
else:
    print()
    print("ERROR: Invalid Operator or Input!")

print()
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

if (firstNum.isalpha() == False) and (secondNum.isalpha() == False):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        intFirstNum = int(firstNum)
        intSecNum = int(secondNum)
        print()
        result = 0
        if operator == '+':
            result = add(intFirstNum, intSecNum)
        if operator == '-':
            result = subtract(intFirstNum, intSecNum)
        if operator == '*':
            result = mult(intFirstNum, intSecNum)
        if operator == '/':
            result = div(intFirstNum, intSecNum)
        print(firstNum, operator, secondNum, "=", str(result))
    else:
        print()
        print("ERROR: Invalid Operator!")
else:
    print()
    print("ERROR: Invalid Input!")

print()
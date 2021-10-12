def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print()
firstNum = input("Enter the first number: ")
operator = input("Enter the operator: ")
secondNum = input("Enter the second number: ")

if operator != '+' or '-' or '*' or '/':
    print("ERROR: Invalid Operator!")
elif operator == '+':
    print('x', firstNum)

print()
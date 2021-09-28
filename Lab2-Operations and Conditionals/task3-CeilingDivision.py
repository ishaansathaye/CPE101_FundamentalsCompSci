def ceiling(x, y):
    if ((x % y) == 0):
        quotient = x / y
    else:
        quotient = int(x) // int(y)
        quotient = quotient + 1
    return quotient

print()
number1 = input("Enter the numerator: ")
number2 = input("Enter the denominator: ")
print()
print("Ceiling:", ceiling(int(number1), int(number2)))
print("Division:", (int(number1)/int(number2)))
print("Floor:", (int(number1) // int(number2)))
print()

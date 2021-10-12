#Factorial Recursion
def factorial(x):
    if x == 1:
        return x
    return x*factorial(x-1)

print()
number = int(input("Enter a number: "))
if number < 0:
    print("ERROR: Negative number!")
elif number == 0:
    print("1")
else:
    print(str(number) + "! is", factorial(number))

#Fibonacci Sequence Recursion
def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N-1)+fibonacci(N-2)

print()
for i in range(0,11):
    print("N=" + str(i), "->", str(fibonacci(i)))
print()
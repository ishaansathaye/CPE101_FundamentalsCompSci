import math as m

def calcExponential(x):
    result = 1 + x
    n = 2
    while True:
        prev = result
        result = result + ((x**n)/m.factorial(n))
        if round(prev, 4) == round(result, 4):
            break
        n = n + 1
    return round(result, 2)

print()
num = float(input("Enter a number: "))
print("e^"+str(num) + ": " + str(calcExponential(num)))
print()

def test_calcExponential():
    assert calcExponential(4) == round(m.exp(4), 2), "Should be 54.6"
    
test_calcExponential()
print("Everything Passed.")
print()
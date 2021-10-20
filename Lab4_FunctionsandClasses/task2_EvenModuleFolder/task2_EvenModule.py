def is_even(num):
    while True:
        try:
            if num == float(num):
                break
        except ValueError:
            print()
            print("Please enter a number only!")
            num = int(input("Enter a number: "))
            print()
            continue
        break
    if num % 2 == 0:
        return True
    else:
        return False



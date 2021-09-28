print()
user_string = input("Enter a 5-letter word: ")
print()

listString = list(user_string)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

stringCheck = any(i in listString for i in numbers)

if (len(user_string) != 5) or stringCheck == True:
  print('Error')
  print()
else:
    reverseString = user_string[::-1]
    print("Reverse of String:", reverseString)
    print()
    if user_string == reverseString:
        print(user_string, "IS a palindrome!")
        print()
    else:
        print(user_string, "is NOT a palindrome!")
        print()
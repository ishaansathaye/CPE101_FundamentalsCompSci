def print_palindrome():
    def is_palindrome(user_string):
        reverseString = user_string[::-1]
        if user_string == reverseString:
            return True
        else:
            return False
    wordList = []
    palList = []
    finalGate = True
    for i in range(0, 3):
        inputWord = input("Enter a 5-letter word: ")
        wordList.append(inputWord)
    for j in range(0, (len(wordList))):
        word = wordList[j]
        if len(word) != 5:
            print()
            print("ERROR: one or more input is not a 5-letter word!")
            print()
            finalGate = False
            break
        elif ((is_palindrome(word)) == True):
            palList.append(word)
    if finalGate == True:
        if (len(palList) == 0):
            print()
            print("No palindromes were found!")
        else:
            print()
            for item in palList:
                print(item, "is a palindrome!")
        print()

print_palindrome()
      
    
  
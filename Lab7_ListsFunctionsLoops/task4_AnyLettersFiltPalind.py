words = ['kayak', 'zebra', 'madam', 'civic', 'tacocat', 'stops']

def is_palindrome(word):
    reverseWord = word[::-1]
    if word == reverseWord:
        return True
    else:
        return False

def filter_palindromes(wordList):
    palindromeList = []
    for word in wordList:
        if is_palindrome(word) == True:
            palindromeList.append(word)
    return palindromeList

print()
print("Palindromes found:", end=" ")
for item in filter_palindromes(words):
    print(item, end=" ")
print("\n")

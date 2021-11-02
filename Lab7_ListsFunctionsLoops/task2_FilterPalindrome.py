words = ['kayak', 'zebra', 'madam', 'civic', 'apart', 'stops']

def is_palindrome(word):
    if word[0] == word[4] and word[1] == word[3]:
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
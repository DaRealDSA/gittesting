# Palindrome word check

def Palindrome(word):
    # Gets the last index
    right = len(word) - 1

    if len(word) <= 1: return True

    # Loops every left and last index
    for left in range(len(word)):

        # Checks if the lefts are matched, otherwise its terminated
        if not word[left] == word[right]:
            break

        # Checks if the middle index left matches the 'right' letter
        if right == left: return True

        # Decrement
        right -= 1

    # Return False if palindrome word isn't matched exactly
    return False

palin_word = input("Enter word: ")
# Finally prints the result
print(Palindrome(palin_word))
def isPalindrome(string):
    isPal = True
    for i in range(len(string)):
        if string[i] != string[-(i+1)]:
            isPal = False
            break
    return isPal

print(isPalindrome("rotator"))
print(isPalindrome("word"))
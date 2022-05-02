s = "abca"

def checkPalindrome(s ,  start , end):

    if (start>=end):
        return True
    return (s[start] == s[end]) and checkPalindrome(s, start+1 , end-1)

print(checkPalindrome(s  , 0 , end = len(s)-1))
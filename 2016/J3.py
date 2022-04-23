def isPalindrome(s):
    if len(s) == 1:
        return True
    t =s[::-1]
    if t == s:
        return True
    return False

def findAllSubstrings(l, s):
    substrs = []
    l-=1
    for i in range(l, len(s)):
        substrs.append(s[i - l:i+1])
    return substrs

m = -2147483647
string = input()
for i in range(1, len(string)+1):
    s = findAllSubstrings(i, string)
    for x in s:
        if isPalindrome(x) and len(x) > m:
            m = len(x)
print(m)
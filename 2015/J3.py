import sys
input = sys.stdin.readline
consonants = 'bcdfghjklmnpqrstvwxyzz'
vals = {'b':'a','c':'a','d':'e','f':'e','g':'e','h':'i','j':'i','k':'i','l':'i','m':'o','n':'o','p':'o','q':'o','r':'o','s':'u','t':'u','v':'u','w':'u','x':'u','y':'u','z':'u'}

word = input()
new = ''
for c in word:
    if c in consonants:
        new += c
        new += vals[c]
        new += consonants[consonants.index(c) + 1]
    else: new += c
print(new)
doubles = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key = input()
encoded = input()
encoded = ''.join(e for e in encoded if e.isalnum())

substrs = []
for i in range(0, len(encoded), len(key)):
    substrs.append(encoded[i:i+len(key)])

for strs in range(len(substrs)):
    temp = ""
    for s in range(len(substrs[strs])):
        temp += doubles[doubles.index(substrs[strs][s]) + doubles.index(key[s])]
    substrs[strs] = temp
print(''.join(substrs))
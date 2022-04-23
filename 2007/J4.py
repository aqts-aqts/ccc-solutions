s1 = input().replace(' ','')
s2 = input().replace(' ','')

counts1 = dict()
counts2 = dict()

if len(s1) == len(s2):
    for s in range(len(s1)):
        if not s1[s] in counts1:
            counts1[s1[s]] = 1
        else:
            counts1[s1[s]] += 1
        if not s2[s] in counts2:
            counts2[s2[s]] = 1
        else:
            counts2[s2[s]] += 1

    if counts1 == counts2:
        print("Is an anagram.")
    else:
        print("Is not an anagram.")
else:
    print("Is not an anagram.")

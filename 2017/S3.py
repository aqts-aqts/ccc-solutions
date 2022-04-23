n = int(input())
boards = [int(x) for x in input().split()]

lengths = [0] * 2001
pairs = [0] * 4001

for b in boards:
    lengths[b] += 1 

for i in range(len(lengths) - 1):
    for j in range(i, len(lengths)):
        if i == j:
            pairs[i + j] += lengths[i] // 2
        else:
            pairs[i + j] += min(lengths[i], lengths[j])

maxLength = 0
maxAmount = 0
for length in pairs:
    if length > maxLength:
        maxLength = length
        maxAmount = 1
    elif length == maxLength:
        maxAmount += 1

print(maxLength, maxAmount)
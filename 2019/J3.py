totalLines = int(input())
lines = []
for v in range(totalLines):
    temp = input()
    lines.append(temp)

countedLines = []
for line in lines:
    count = 0
    prevChar = line[0]
    tempHolder = []
    for char in range(len(line)):
        if line[char] == prevChar:
            count += 1
        else:
            tempHolder.append([count, prevChar])
            count = 1

        if char == len(line) - 1:
            if count == 1 and len(line) - 1:
                tempHolder.append([count, line[char]])
            else:
                tempHolder.append([count, prevChar])
        prevChar = line[char]
    temp = []
    for v in tempHolder:
        for x in v:
            temp.append(x)
    countedLines.append(temp)

for v in countedLines:
    for x in v:
        print(str(x) + ' ', end = '')
    print()
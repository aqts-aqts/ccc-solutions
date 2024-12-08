word = input()
r = int(input())
c = int(input())
grid = []
for _ in range(r):
    grid.append(list(input()))
searchMap = {}
for i, char in enumerate(word):
    searchMap[char] = i + 1

gridMap = [[None] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        char = grid[i][j]
        if char in searchMap:
            gridMap[i][j] = searchMap[char]
        else:
            gridMap[i][j] = 0

dx = [1, -1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def findWord(row, col, cur = 1, d = None, turned = False):
    total = 0
    if gridMap[row][col] == len(word): 
        total = 1
    elif d is None:
        for i in range(8):
            x = col + dx[i]
            y = row + dy[i]
            if x < 0 or x > c - 1 or y < 0 or y > r - 1: 
                continue
            if gridMap[y][x] == cur + 1:
                total += findWord(y, x, cur + 1, i, turned)
    else:
        x = col + dx[d]
        y = row + dy[d]
        if x >= 0 and x <= c - 1 and y >= 0 and y <= r - 1 and gridMap[y][x] == cur + 1:
            total = findWord(y, x, cur + 1, d)
        if not turned:
            turns = None
            if dy[d] and not dx[d]:
                turns = (0, 1)
            elif dx[d] and not dy[d]:
                turns = (2, 3)
            elif dx[d] == dy[d]:
                turns = (4, 5)
            else:
                turns = (6, 7)
            for turn in turns:
                x = col + dx[turn]
                y = row + dy[turn]
                if x >= 0 and x <= c - 1 and y >= 0 and y <= r - 1 and gridMap[y][x] == cur + 1:
                    total += findWord(y, x, cur + 1, turn, not turned)
    return total

words = 0
for i in range(r):
    for j in range(c):
        if gridMap[i][j] == 1:
            words += findWord(i, j)
print(words)
import sys
input = sys.stdin.readline
r = int(input())
c = int(input())
grid = []
for i in range(r):
    grid.append(input().strip())
m = int(input())
actions = []
for i in range(m):
    actions.append(input().strip())

directions = 'nsew'
possibles = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            continue
        for d in directions:
            coords = [i, j]
            currentdir = d
            for a in actions:
                try:
                    if grid[coords[0]][coords[1]] == 'X':
                        break
                except:
                    break
                if a == 'F' and currentdir == 'n':
                    coords[0] -= 1
                elif a == 'F' and currentdir == 's':
                    coords[0] += 1
                elif a == 'F' and currentdir == 'e':
                    coords[1] += 1
                elif a == 'F' and currentdir == 'w':
                    coords[1] -= 1
                elif a == 'R' and currentdir == 'n':
                    currentdir = 'e'
                elif a == 'R' and currentdir == 's':
                    currentdir = 'w'
                elif a == 'R' and currentdir == 'e':
                    currentdir = 's'
                elif a == 'R' and currentdir == 'w':
                    currentdir = 'n'
                elif a == 'L' and currentdir == 'n':
                    currentdir = 'w'
                elif a == 'L' and currentdir == 's':
                    currentdir = 'e'
                elif a == 'L' and currentdir == 'e':
                    currentdir = 'n'
                elif a == 'L' and currentdir == 'w':
                    currentdir = 's'
            if coords[0] >= 0 and coords[0] < r and coords[1] >= 0 and coords[1] < c and grid[coords[0]][coords[1]] != 'X':
                grid[coords[0]] = grid[coords[0]][:coords[1]] + '*' + grid[coords[0]][coords[1] + 1:]
for row in grid:
    print(row)
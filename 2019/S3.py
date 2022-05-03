import sys
from copy import deepcopy
input = sys.stdin.readline

def col(grid, c):
    col = [g[c] for g in grid.copy()]
    return col

def fill(grid):
    current = deepcopy(grid)
    for i in range(3):
        for j in range(3):
            rows = grid[i].count(None)
            cols = col(grid, j).count(None) == 1
            if grid[i][j] == None and (rows == 1 or cols == 1):
                if rows == 1: 
                    if j == 0: grid[i][j] = grid[i][1] - (grid[i][2] - grid[i][1])
                    if j == 1: grid[i][j] = grid[i][0] + (grid[i][2] - grid[i][0]) / 2
                    if j == 2: grid[i][j] = grid[i][1] + (grid[i][1] - grid[i][0])
                else:
                    if i == 0: grid[i][j] = grid[1][j] - (grid[2][j] - grid[1][j])
                    if i == 1: grid[i][j] = grid[0][j] + (grid[2][j] - grid[0][j]) / 2
                    if i == 2: grid[i][j] = grid[1][j] + (grid[1][j] - grid[0][j])
    if grid != current: fill(grid)

def fillLayers(grid):
    for i in range(3): 
        if grid[i].count(None) == 0: row = i
        if col(grid, i).count(None) == 0: coln = i
    if row <= 1: d = grid[row + 1][coln] - grid[row][coln]
    elif row == 2: d = grid[1][coln] - grid[0][coln]

    for i in range(3):
        for j in range(3):
            if i == row or j == coln: continue
            if grid[i][j] == None:
                if i == 0: grid[i][j] = grid[row][j] - d * row
                if i == 1: grid[i][j] = grid[row][j] + d if row == 0 else grid[row][j] - d
                if i == 2: grid[i][j] = grid[row][j] + d * (2 - row)

def solve(grid, case):
    if case == 0: return [[0] * 3] * 3
    elif case == 1:
        for i in range(3):
            for j in range(3):
                if grid[i][j] != None: return [[grid[i][j]] * 3] * 3
    elif case == 2:
        fill(grid)
        for i in range(3):
            if grid[i].count(None) == 0: return [grid[i]] * 3
            if col(grid, i).count(None) == 0: return [[grid[0][i]] * 3, [grid[1][i]] * 3, [grid[2][i]] * 3]
    elif case == 3:
        fill(grid)
        fillLayers(grid)
        return grid
    elif case == 4:
        fill(grid)
        return grid
    elif case == 5:
        grid[1][0] = grid[1][1]
        fill(grid)
        return grid
    elif case == 6:
        grid[1][1] = grid[2][1] if grid[2][1] != None else grid[0][1]
        fill(grid)
        return grid
    else:
        cur = deepcopy(grid)
        isRow = True
        for row in range(3):
            for c in range(3):
                if grid[row][c] != None: grid[row] = [grid[row][c]] * 3; break
        fill(grid)
        for row in range(3):
            for c in range(3):
                if int(grid[row][c]) != grid[row][c]: isRow = False
        if isRow: return grid

        grid = deepcopy(cur)
        for row in range(3):
            for c in range(3):
                if grid[row][c] != None: 
                    for i in range(3): grid[i][c] = grid[row][c]
        fill(grid)
        return grid


grid = []
for _ in range(3): grid.append([int(i) if i != 'X' else None for i in input().split()])
rows = 0; cols = 0
fills = grid.copy()
fill(fills)
for i in range(3):
    if fills[i].count(None) == 0: rows += 1
    if col(fills, i).count(None) == 0: cols += 1

gridMap = []
for i in range(3): gridMap.append([1 if type(cell) is int else 0 for cell in grid[i]])

if sum([row.count(None) for row in grid]) == 9: case = 0
elif sum([row.count(None) for row in grid]) == 8: case = 1
elif rows == 1 and cols == 0 or rows == 0 and cols == 1: case = 2
elif rows == 1 and cols == 1: case = 3
elif rows >= 2 or cols >= 2: case = 4
elif gridMap == [[1,0,0],[0,1,0],[0,0,1]] or gridMap == [[0,0,1],[0,1,0],[1,0,0]]: case = 5
elif gridMap == [[1,0,0],[0,0,1],[0,1,0]] or gridMap == [[0,1,0],[0,0,1],[1,0,0]] or gridMap == [[0,1,0],[1,0,0],[0,0,1]] or gridMap == [[0,0,1],[1,0,0],[0,1,0]]: case = 6
else: case = 7

for row in solve(grid, case): print(int(row[0]), int(row[1]), int(row[2]))
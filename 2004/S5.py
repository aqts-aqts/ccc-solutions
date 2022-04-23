import sys
input = sys.stdin.readline

r, c = map(int, input().split())
while r != 0:
    y = [[-1 for i in range(c)] for j in range(r)]
    grid = []
    for i in range(r):
        grid.append([0 if i == '.' else -1 if i == '*' else int(i) for i in input().strip()])
    y[r - 1][0] = grid[r - 1][0]
    for i in range(r - 2, -1, -1):
        if grid[i][0] >= 0:
            y[i][0] = y[i + 1][0] + grid[i][0]
        else:
            break

    for col in range(1, c):
        for row in range(r):
            coins = y[row][col - 1]
            if y[row][col - 1] >= 0:
                for i in range(row, r):
                    if grid[i][col] >= 0:
                        coins += grid[i][col]
                        if coins > y[i][col]:
                            y[i][col] = coins
                    else:
                        break
        for row in range(r - 1, -1, -1):
            if y[row][col - 1] >= 0:
                coins = y[row][col - 1]
                for i in range(row, -1, -1):
                    if grid[i][col] >= 0:
                        coins += grid[i][col]
                        if coins > y[i][col]:
                            y[i][col] = coins
                    else:
                        break
    print(y[r - 1][c - 1])
    r, c = map(int, input().split())
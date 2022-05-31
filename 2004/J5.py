import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
level, width, x = map(int, input().split())
fractal = [[0] * (width) for _ in range(width // 2)]
def spread(x1, x2, y1, y2, lvl, dir):
    size = y2 - y1
    if dir == 0: # upwards
        for i in range(y2, y2 + size // 3): # top
            for j in range(x1 + size // 3, x2 - size // 3):
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y2, y2 + size // 3, lvl + 1, 0)
        for i in range(y1 + size // 3, y2 - size // 3):
            for j in range(x1 - size // 3, x1): # left mid
                fractal[i][j] = 1
            for j in range(x2, x2 + size // 3): # right mid
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 - size // 3, x1, y1 + size // 3, y2 - size // 3, lvl + 1, 1)
        if lvl + 1 < level: spread(x2, x2 + size // 3, y1 + size // 3, y2 - size // 3, lvl + 1, 2)
        for i in range(y1, y1 + size // 3):
            for j in range(x1 - 2 * size // 3, x1 - size // 3): # left bottom
                fractal[i][j] = 1
            for j in range(x2 + size // 3, x2 + 2 * size // 3): # right bottom
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 - 2 * size // 3, x1 - size // 3, y1, y1 + size // 3, lvl + 1, 0)
        if lvl + 1 < level: spread(x2 + size // 3, x2 + 2 * size // 3, y1, y1 + size // 3, lvl + 1, 0)
    elif dir == 1: # left
        for i in range(y1 + size // 3, y2 - size // 3): # left
            for j in range(x1 - size // 3, x1):
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 - size // 3, x1, y1 + size // 3, y2 - size // 3, lvl + 1, 1)
        for i in range(x1 + size // 3, x2 - size // 3):
            for j in range(y1 - size // 3, y1): # up mid
                fractal[j][i] = 1
            for j in range(y2, y2 + size // 3): # down mid
                fractal[j][i] = 1
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y1 - size // 3, y1, lvl + 1, 3)
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y2, y2 + size // 3, lvl + 1, 1)
        for i in range(x2 - size // 3, x2):
            for j in range(y1 - 2 * size // 3, y1 - size // 3): # down right
                fractal[j][i] = 1
            for j in range(y2 + size // 3, y2 + 2 * size // 3): # up right
                fractal[j][i] = 1
        if lvl + 1 < level: spread(x2 - size // 3, x2, y1 - 2 * size // 3, y1 - size // 3, lvl + 1, 1)
        if lvl + 1 < level: spread(x2 - size // 3, x2, y2 + size // 3, y2 + 2 * size // 3, lvl + 1, 1)
    elif dir == 2: # right
        for i in range(y1 + size // 3, y2 - size // 3): # right
            for j in range(x2, x2 + size // 3):
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x2, x2 + size // 3, y1 + size // 3, y2 - size // 3, lvl + 1, 2)
        for i in range(x1 + size // 3, x2 - size // 3):
            for j in range(y1 - size // 3, y1): # up mid
                fractal[j][i] = 1
            for j in range(y2, y2 + size // 3): # down mid
                fractal[j][i] = 1
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y1 - size // 3, y1, lvl + 1, 3)
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y2, y2 + size // 3, lvl + 1, 1)
        for i in range(x1, x1 + size // 3):
            for j in range(y1 - 2 * size // 3, y1 - size // 3): # down left
                fractal[j][i] = 1
            for j in range(y2 + size // 3, y2 + 2 * size // 3): # up left
                fractal[j][i] = 1
        if lvl + 1 < level: spread(x1, x1 + size // 3, y1 - 2 * size // 3, y1 - size // 3, lvl + 1, 2)
        if lvl + 1 < level: spread(x1, x1 + size // 3, y2 + size // 3, y2 + 2 * size // 3, lvl + 1, 2)
    else: # down
        for i in range(y1 - size // 3, y1): # bottom
            for j in range(x1 + size // 3, x2 - size // 3):
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 + size // 3, x2 - size // 3, y1 - size // 3, y1, lvl + 1, 3)
        for i in range(y1 + size // 3, y2 - size // 3):
            for j in range(x1 - size // 3, x1): # left mid
                fractal[i][j] = 1
            for j in range(x2, x2 + size // 3): # right mid
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 - size // 3, x1, y1 + size // 3, y2 - size // 3, lvl + 1, 1)
        if lvl + 1 < level: spread(x2, x2 + size // 3, y1 + size // 3, y2 - size // 3, lvl + 1, 2)
        for i in range(y2 - size // 3, y2):
            for j in range(x1 - 2 * size // 3, x1 - size // 3): # left top
                fractal[i][j] = 1
            for j in range(x2 + size // 3, x2 + 2 * size // 3): # right top
                fractal[i][j] = 1
        if lvl + 1 < level: spread(x1 - 2 * size // 3, x1 - size // 3, y2 - size // 3, y2, lvl + 1, 3)
        if lvl + 1 < level: spread(x2 + size // 3, x2 + 2 * size // 3, y2 - size // 3, y2, lvl + 1, 3)

length = width // 3
if level > 0:
    for i in range(width // 3):
        for j in range(width // 3, width - width // 3):
            fractal[i][j] = 1
    spread(width // 3, width - width // 3, 0, width // 3, 1, 0)
    lines = [[] for _ in range(width)]
    for i in range(width):
        for j in range(width):
            try: 
                if fractal[i][j - 1] != fractal[i][j]: lines[j].append(i + 1); continue
            except: pass
            try: 
                if fractal[i - 1][j] != fractal[i][j]: lines[j].append(i + 1); continue
            except: pass
            try: 
                if fractal[i - 1][j - 1] != fractal[i][j]: lines[j].append(i + 1); continue
            except: pass
    try: 
        if fractal[0][x] == 1: lines[x].remove(1)
        else: 
            if 1 not in lines[x]: lines[x].append(1)
    except: pass
    print(' '.join(map(str, sorted(lines[x]))))
else: print('1') # level 0 is nothing
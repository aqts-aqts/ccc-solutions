r = int(input())
c = int(input())
patch = []
for i in range(r):
    patch.append(list(input()))
y = int(input())
x = int(input())

pumpkins = 0

queue = []
queue.append((y, x))
visited = set()
visited.add((y, x))
while queue:
    y, x = queue.pop(0)
    pumpkins += 1 if patch[y][x] == 'S' else 5 if patch[y][x] == 'M' else 10 if patch[y][x] == 'L' else 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < r and 0 <= nx < c and (ny, nx) not in visited and patch[ny][nx] != '*':
            visited.add((ny, nx))
            queue.append((ny, nx))

print(pumpkins)
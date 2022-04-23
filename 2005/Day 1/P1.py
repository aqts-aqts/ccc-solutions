from queue import PriorityQueue
import sys
input = sys.stdin.readline

cols, rows = map(int, input().split())
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split())))

def bfs(s):
    queue = PriorityQueue()
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    if s < 0: 
        for i in range(cols): queue.put((matrix[0][i], [(0, i), {matrix[0][i]}]))
    else: queue.put((matrix[0][s], [(0, s), {matrix[0][s]}]))
    while not queue.empty():
        front = queue.get()[1]
        pos = front[0]; nodes = front[1].copy()
        if pos[0] == rows - 1: return nodes
        if pos[0] + 1 < rows and not visited[pos[0] + 1][pos[1]]: 
            down = nodes.copy(); down.add(matrix[pos[0] + 1][pos[1]])
            if len(down) <= 3:
                queue.put((matrix[pos[0] + 1][pos[1]], [(pos[0] + 1, pos[1]), down]))
                visited[pos[0] + 1][pos[1]] = True
        if pos[0] - 1 >= 0 and not visited[pos[0] - 1][pos[1]]:
            up = nodes.copy(); up.add(matrix[pos[0] - 1][pos[1]]) 
            if len(up) <= 3:
                queue.put((matrix[pos[0] - 1][pos[1]], [(pos[0] - 1, pos[1]), up]))
                visited[pos[0] - 1][pos[1]] = True
        if pos[1] + 1 < cols and not visited[pos[0]][pos[1] + 1]:
            right = nodes.copy(); right.add(matrix[pos[0]][pos[1] + 1]) 
            if len(right) <= 3:
                queue.put((matrix[pos[0]][pos[1] + 1], [(pos[0], pos[1] + 1), right]))
                visited[pos[0]][pos[1] + 1] = True
        if pos[1] - 1 >= 0 and not visited[pos[0]][pos[1] - 1]:
            left = nodes.copy(); left.add(matrix[pos[0]][pos[1] - 1]) 
            if len(left) <= 3:
                queue.put((matrix[pos[0]][pos[1] - 1], [(pos[0], pos[1] - 1), left]))
                visited[pos[0]][pos[1] - 1] = True
    return False

path = bfs(-1)
if path: s = sorted(list(path)); print('0 ' * (3 - len(path)) + ' '.join(list(map(str, s))))
else:
    paths = []
    for i in range(cols):
        path = bfs(i)
        if path: paths.append(sorted(list(path)))
    if len(paths) > 0: s = sorted(paths)[0]; print('0 ' * (3 - len(s)) + ' '.join(list(map(str, s))))
    else: print('-1 -1 -1')
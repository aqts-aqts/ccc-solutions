from queue import PriorityQueue
import sys 
input = sys.stdin.readline

def BFS(matrix):
    n = len(matrix)
    queue = PriorityQueue()
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    distance[0][0] = 0
    queue.put((0, (0, 0)))
    visited[0][0] = True
    w = matrix[0][0]
    while not queue.empty():
        pos = queue.get()[1]
        v = matrix[pos[0]][pos[1]]
        if pos[0] - 1 >= 0 and abs(matrix[pos[0] - 1][pos[1]] - v) <= 2 and not visited[pos[0] - 1][pos[1]]:
            visited[pos[0] - 1][pos[1]] = True
            if matrix[pos[0] - 1][pos[1]] > w or v > w: distance[pos[0] - 1][pos[1]] = distance[pos[0]][pos[1]] + 1
            else: distance[pos[0] - 1][pos[1]] = distance[pos[0]][pos[1]]
            queue.put((distance[pos[0] - 1][pos[1]], (pos[0] - 1, pos[1])))
        if pos[0] + 1 < n and abs(matrix[pos[0] + 1][pos[1]] - v) <= 2 and not visited[pos[0] + 1][pos[1]]:
            visited[pos[0] + 1][pos[1]] = True
            if matrix[pos[0] + 1][pos[1]] > w or v > w: distance[pos[0] + 1][pos[1]] = distance[pos[0]][pos[1]] + 1
            else: distance[pos[0] + 1][pos[1]] = distance[pos[0]][pos[1]]
            queue.put((distance[pos[0] + 1][pos[1]], (pos[0] + 1, pos[1])))
        if pos[1] - 1 >= 0 and abs(matrix[pos[0]][pos[1] - 1] - v) <= 2 and not visited[pos[0]][pos[1] - 1]:
            visited[pos[0]][pos[1] - 1] = True
            if matrix[pos[0]][pos[1] - 1] > w or v > w: distance[pos[0]][pos[1] - 1] = distance[pos[0]][pos[1]] + 1
            else: distance[pos[0]][pos[1] - 1] = distance[pos[0]][pos[1]]
            queue.put((distance[pos[0]][pos[1] - 1], (pos[0], pos[1] - 1)))
        if pos[1] + 1 < n and abs(matrix[pos[0]][pos[1] + 1] - v) <= 2 and not visited[pos[0]][pos[1] + 1]:
            visited[pos[0]][pos[1] + 1] = True
            if matrix[pos[0]][pos[1] + 1] > w or v > w: distance[pos[0]][pos[1] + 1] = distance[pos[0]][pos[1]] + 1
            else: distance[pos[0]][pos[1] + 1] = distance[pos[0]][pos[1]]
            queue.put((distance[pos[0]][pos[1] + 1], (pos[0], pos[1] + 1)))
    return distance[n - 1][n - 1]

trips = int(input())
for t in range(trips):
    n = int(input())
    terrain = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            terrain[i][j] = int(input())
    dist = BFS(terrain)
    if dist == -1: print('CANNOT MAKE THE TRIP')
    else: print(dist)
    if t != trips - 1: print()

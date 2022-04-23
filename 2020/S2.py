import math

m = int(input())
n = int(input())
graph = []
found = False

for i in range(m):
    graph.append([int(x) for x in input().split()])

def findNodes(num):
    pairs = []
    for i in range(1, math.ceil(math.sqrt(num) + 1)):
        if num % i == 0:
            p = num // i
            if (i == m and p == n or i == n and p == m):
                global found
                found = True

            if (i <= m and p <= n):
                pairs.append((i, p))
            if (i <= n and p <= m):
                pairs.append((p, i))
    return pairs

def BFS():
    visited = dict()
    queue = []

    queue.append((1, 1))
    visited[(1, 1)] = True
    while queue:
        global found
        if found:
            return "yes"

        front = queue.pop(0)

        if front == (m, n):
            return "yes"

        for f in findNodes(graph[front[0] - 1][front[1] - 1]):
            if not f in visited:
                queue.append(f)
                visited[f] = True
    return "no"

print(BFS())
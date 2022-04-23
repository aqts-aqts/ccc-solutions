import sys
input = sys.stdin.readline
from collections import defaultdict
def isPath(graph, start, target):
    visited = defaultdict(lambda: False)
    queue = []

    queue.append(start)
    visited[start] = True
    while queue:
        front = queue.pop(0)
        for node in graph[front]:
            if node == target:
                return True

            if not visited[node]:
                queue.append(node)
                visited[node] = True
    return False

n, m = map(int, input().split())
heights = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    heights[x].append(y)
p, q = map(int, input().split())

yes = isPath(heights, p, q)
no = isPath(heights, q, p)

if yes:
    print("yes")
elif no:
    print("no")
else:
    print("unknown")
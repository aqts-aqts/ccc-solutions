from collections import defaultdict as dd

leafLayer = 0
def DFS(graph, start, layer, visited = None):
    if visited is None: visited = set()
    global leafLayer
    visited.add(start)
    for n in graph[start] - visited:
        DFS(graph, n, layer + 1, visited)
    leafLayer = max(layer, leafLayer)
    

l = int(input())
results = []
for _ in range(l):
    n = int(input())
    graph = dd(set)
    prev = input()
    for _ in range(n - 1):
        cur = input()
        graph[prev].add(cur)
        graph[cur].add(prev)
        prev = cur
    leafLayer = 0
    DFS(graph, prev, 0)
    results.append(n * 10 - leafLayer * 20)
for result in results:
    print(result)
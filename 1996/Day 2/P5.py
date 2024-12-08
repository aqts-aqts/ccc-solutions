from collections import defaultdict, deque

n, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(n):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

for _ in range(k):
    a, b = input().split()
    visited = set()
    queue = deque([a])
    path = deque([a[0]])
    while queue:
        node = queue.popleft()
        current_path = path.popleft()
        if node == b:
            print(''.join(current_path))
            break
        
        for neighbour in graph[node]:
            if not neighbour in visited:
                queue.append(neighbour)
                path.append(current_path + neighbour[0])
                visited.add(neighbour)
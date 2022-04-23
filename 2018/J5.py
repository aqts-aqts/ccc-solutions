n = int(input())
pages = [[]]
for i in range(n):
    x = [int(it) for it in input().split() if it != 0]
    x.pop(0)
    pages.append(x)

def findShortestPath():
    visited = [False] * len(pages)
    dist = [0] * len(pages)
    exits = []
    queue = [[1, 0]]
    nodes = [1]

    visited[1] = True
    while queue:
        front = queue.pop(0)
        if front[1] > 0:
            dist[front[0]] += dist[front[1]] + 1

        if len(pages[front[0]]) == 0:
            exits.append(dist[front[0]])

        for f in pages[front[0]]:
            if visited[f] == False:
                nodes.append(f)
                queue.append([f, front[0]])
                visited[f] = True
    return [nodes, exits]

result = findShortestPath()
flag = True
for i in range(1, n):
    if not(i in result[0]):
        flag = False
        break

if flag:
    print("Y")
    print(min(result[1]) + 1)
else:
    print("N")
    print(min(result[1]) + 1)
def findShortestPath(graph, rows, cols):
    visited = [[False for i in range(cols)] for j in range(rows)]
    queue = []

    visited[0][0] = True
    queue.append([(0, 0), 1])
    while queue:
        front = queue.pop(0)
        if front[0] == (rows - 1, cols - 1):
            return front[1]
        
        if graph[front[0][0]][front[0][1]] == '+':
            if front[0][0] - 1 >= 0 and graph[front[0][0] - 1][front[0][1]] != '*' and not visited[front[0][0] - 1][front[0][1]]:
                queue.append([(front[0][0] - 1, front[0][1]), front[1] + 1])
                visited[front[0][0] - 1][front[0][1]] = True
            if front[0][1] - 1 >= 0 and graph[front[0][0]][front[0][1] - 1] != '*' and not visited[front[0][0]][front[0][1] - 1]:
                queue.append([(front[0][0], front[0][1] - 1), front[1] + 1])
                visited[front[0][0]][front[0][1] - 1] = True
            if front[0][0] + 1 < rows and graph[front[0][0] + 1][front[0][1]] != '*' and not visited[front[0][0] + 1][front[0][1]]:
                queue.append([(front[0][0] + 1, front[0][1]), front[1] + 1])
                visited[front[0][0] + 1][front[0][1]] = True
            if front[0][1] + 1 < cols and graph[front[0][0]][front[0][1] + 1] != '*' and not visited[front[0][0]][front[0][1] + 1]:
                queue.append([(front[0][0], front[0][1] + 1), front[1] + 1])
                visited[front[0][0]][front[0][1] + 1] = True
        elif graph[front[0][0]][front[0][1]] == '-':
            if front[0][1] - 1 >= 0 and graph[front[0][0]][front[0][1] - 1] != '*' and not visited[front[0][0]][front[0][1] - 1]:
                queue.append([(front[0][0], front[0][1] - 1), front[1] + 1])
                visited[front[0][0]][front[0][1] - 1] = True
            if front[0][1] + 1 < cols and graph[front[0][0]][front[0][1] + 1] != '*' and not visited[front[0][0]][front[0][1] + 1]:
                queue.append([(front[0][0], front[0][1] + 1), front[1] + 1])
                visited[front[0][0]][front[0][1] + 1] = True
        elif graph[front[0][0]][front[0][1]] == '|':
            if front[0][0] - 1 >= 0 and graph[front[0][0] - 1][front[0][1]] != '*' and not visited[front[0][0] - 1][front[0][1]]:
                queue.append([(front[0][0] - 1, front[0][1]), front[1] + 1])
                visited[front[0][0] - 1][front[0][1]] = True
            if front[0][0] + 1 < rows and graph[front[0][0] + 1][front[0][1]] != '*' and not visited[front[0][0] + 1][front[0][1]]:
                queue.append([(front[0][0] + 1, front[0][1]), front[1] + 1])
                visited[front[0][0] + 1][front[0][1]] = True
    return -1

t = int(input())
for i in range(t):
    r = int(input())
    c = int(input())
    graph = []
    for j in range(r):
        graph.append(input())
    print(findShortestPath(graph, r, c))
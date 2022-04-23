flooring = int(input())
rows = int(input())
columns = int(input())

def BFS(house, y, x):
    visited = [[False] * 25 for i in range(25)]
    queue = []
    nodes = []
    
    visited[y][x] = True
    queue.append([y, x])
    nodes.append([y, x])
    while queue:
        front = queue.pop(0)
        if front[1] < columns - 1:
            if not(visited[front[0]][front[1] + 1]) and house[front[0]][front[1] + 1] == '.':
                queue.append([front[0], front[1] + 1])
                visited[front[0]][front[1] + 1] = True
                nodes.append([front[0], front[1] + 1])
        
        if front[0] < rows - 1:
            if not(visited[front[0] + 1][front[1]]) and house[front[0] + 1][front[1]] == '.':
                queue.append([front[0] + 1, front[1]])
                visited[front[0] + 1][front[1]] = True
                nodes.append([front[0] + 1, front[1]])

        if front[1] > 0:
            if not(visited[front[0]][front[1] - 1]) and house[front[0]][front[1] - 1] == '.':
                queue.append([front[0], front[1] - 1])
                visited[front[0]][front[1] - 1] = True
                nodes.append([front[0], front[1] - 1])
        
        if front[0] > 0:
            if not(visited[front[0] - 1][front[1]]) and house[front[0] - 1][front[1]] == '.':
                queue.append([front[0] - 1, front[1]])
                visited[front[0] - 1][front[1]] = True
                nodes.append([front[0] - 1, front[1]])
    return nodes

house = []
rooms = 0
  
for i in range(rows):
    house.append(input())

visited = []
nodes = []
for i in range(rows):
    for j in range(columns):
        if house[i][j] == '.' and [i, j] not in visited:
            room = BFS(house, i, j)
            for r in room:
                visited.append(r)
            nodes.append(len(room))

nodes = sorted(nodes)
nodes.reverse()

for n in nodes:
    if flooring >= n:
        flooring -= n
        rooms += 1
    else:
        break

if rooms != 1:
    print(str(rooms) + " rooms, " + str(flooring) + " square metre(s) left over")
else:
    print("1 room, " + str(flooring) + " square metre(s) left over")
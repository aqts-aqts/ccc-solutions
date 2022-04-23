def oneDimensionalBFS(search, start, target):
    visited = dict()
    queue = []
    
    queue.append([start, -1])
    visited[start] = 1
    while queue:
        front = queue.pop(0)
        if front[0] == target:
            return front[1]
        if front[0] in search and search[front[0]] not in visited:
            queue.append([search[front[0]], front[1] + 1])
    return -1

n = int(input())
friends = dict()
for i in range(n):
    f = input().split()
    friends[int(f[0])] = int(f[1])

find = [int(x) for x in input().split()]
while find != [0, 0]:
    dist = oneDimensionalBFS(friends, find[0], find[1])
    if dist >= 0:
        print("Yes " + str(dist))
    else:
        print("No")
    find = [int(x) for x in input().split()]

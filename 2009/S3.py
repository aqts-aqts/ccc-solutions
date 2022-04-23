friends = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],
          [17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def findShortestPath(source, target):
    visited = [False] * 51
    dist = [0] * 51
    queue = []

    queue.append([source, 0])
    visited[source] = True
    while queue:
        front = queue.pop(0)
        if front[1] > 0:
            dist[front[0]] += dist[front[1]] + 1

        if front[0] == target:
            return dist[front[0]]

        for f in friends[front[0]]:
            if visited[f] == False:
                queue.append([f, front[0]])
                visited[f] = True
    return 'Not connected'

i = input()
while i != 'q':
    if i == 'i':
        x = int(input())
        y = int(input())
        if friends[x].count(y) == 0 and friends[y].count(x) == 0:
            friends[x].append(y)
            friends[y].append(x)
    elif i == 'd':
        x = int(input())
        y = int(input())
        if friends[x].count(y) == 1 and friends[y].count(x) == 1:
            friends[x].remove(y)
            friends[y].remove(x)
    elif i == 'n':
        x = int(input())
        print(len(friends[x]))
    elif i == 'f':
        ff = []
        x = int(input())
        for y in friends[x]:
            for f in friends[y]:
                if ff.count(f) == 0 and f != x and not f in friends[x]:
                    ff.append(f)
        print(len(ff))
    elif i == 's':
        x = int(input())
        y = int(input())
        print(findShortestPath(x, y))
    i = input()
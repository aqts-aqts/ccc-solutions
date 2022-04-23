n = input()
roadmap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
connections = []

def BFS(connection):
    roads = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    connecting = connections.copy()
    connecting.remove(connection)
    for c in connecting:
        roads[c[0]].append(c[1])
        roads[c[1]].append(c[0])
    
    visited = [False] * 26
    nodes = []
    queue = [0]
    while queue:
        front = queue.pop(0)
        for r in roads[front]:
            if visited[r] == False:
                nodes.append(r)
                queue.append(r)
                visited[r] = True
    if 1 not in nodes:
        return True
    return False



while n != "**":
    connections.append((roadmap.index(n[0]), roadmap.index(n[1])))
    n = input()

count = 0
for c in connections:
    if (BFS(c)):
        count += 1
        print(str(roadmap[c[0]]) + str(roadmap[c[1]]))
print("There are " + str(count) + " disconnecting roads.")
from bisect import bisect_left as binarys
import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
distance = lambda p1, p2: (abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2) ** 0.5
search = lambda it, i: 1 if binarys(it, i) < len(it) and it[binarys(it, i)] == i else 0

class Campus:
    def __init__(self, V):
        self.V = V
        self.edges = []
    def addEdge(self, u, v, w):
        self.edges.append((u, v, w))
    def find(self, parent, i):
        if parent[i] == i: return i
        return self.find(parent, parent[i])
    def connect(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        if rank[rootX] < rank[rootY]: parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]: parent[rootY] = rootX
        else: parent[rootY] = rootX; rank[rootX] += 1
    def kruskals(self):
        mst = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda x: x[2])
        parent = [node for node in range(self.V)]
        rank = [0] * self.V
        while e < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                mst.append((u, v, w))
                self.connect(parent, rank, x, y)
        return mst

n = int(input())
campus = Campus(n)
positions = []
for _ in range(n):
    positions.append(tuple(map(int, input().split())))

m = int(input())
points = []
for _ in range(m):
    point = tuple(map(lambda x: int(x) - 1, input().split()))
    points.append(point)
    points.append(point[::-1])
points = sorted(points)

for i in range(n):
    for j in range(i, n):
        if i == j: continue
        if search(points, (i, j)): campus.addEdge(i, j, 0)
        else: campus.addEdge(i, j, distance(positions[i], positions[j]))

mst = campus.kruskals()
print('{:.2f}'.format(sum(edge[2] for edge in mst)))
for u, v, w in mst: 
    if not search(points, (u, v)): print(u + 1, v + 1)
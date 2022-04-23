import sys

class Canal:
    def __init__(self, dest, weight, dmg):
        self.dest = dest
        self.weight = weight
        self.dmg = dmg

class Island:
    def __init__(self):
        self.connections = []
        self.path = sys.maxsize
        self.hull = 0

nodes = [Island() for x in range(10001)]
def findShortestPaths(start, dmg):
    islands = []
    maxHull = []
    distance = []
    nodes[start].path = 0
    
    islands.append(nodes[start])
    maxHull.append(dmg)
    distance.append(0)
    while islands:
        island = islands.pop(0)
        dist = distance.pop(0)
        hull = maxHull.pop(0)

        for c in island.connections:
            nextHull = hull - c.dmg
            nextDist = dist + c.weight
            nextDest = nodes[c.dest]
            if (nextDist < nextDest.path or nextHull > nextDest.hull) and nextHull > 0:
                nextDest.path = min(nextDist, nextDest.path)
                nextDest.hull = max(nextHull, nextDest.hull)

                islands.append(nextDest)
                maxHull.append(nextHull)
                distance.append(nextDist)

k, n, m = map(int, input().split())
for i in range(m):
    a, b, t, h = map(int, input().split())
    nodes[a].connections.append(Canal(b, t, h))
    nodes[b].connections.append(Canal(a, t, h))
start, target = map(int, input().split())
findShortestPaths(start, k)
if nodes[target].path == sys.maxsize:
    print('-1')
else:
    print(nodes[target].path)
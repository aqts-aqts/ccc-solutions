import sys
input = sys.stdin.readline

class Network:
    def __init__(self, computers):
        self.computers = computers
        self.size = len(computers)
    def BFS(self, start, target):
        queue = []; time = []
        visited = [False] * self.size
        queue.append(start); time.append(0)
        visited[start] = True
        while queue:
            front = queue.pop(0)
            travel = time.pop(0)
            if front == target:
                return travel
            for wire in self.computers[front].connections:
                if not visited[wire.computer]:
                    visited[wire.computer] = True
                    queue.append(wire.computer); time.append(travel + wire.packets)
        return False

class Computer:
    def __init__(self):
        self.connections = []
class Wire:
    def __init__(self, computer, packets):
        self.computer = computer
        self.packets = packets

n, w, p = map(int, input().split())
network = Network([Computer() for _ in range(n + 1)])

for _ in range(w): 
    c1, c2, packets = map(int, input().split())
    network.computers[c1].connections.append(Wire(c2, packets))
    network.computers[c2].connections.append(Wire(c1, packets))
for _ in range(p): c1, c2 = map(int, input().split()); print(network.BFS(c1, c2))
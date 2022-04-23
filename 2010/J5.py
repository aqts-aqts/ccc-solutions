class Node:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def BFS(source, target):
    visited = []
    queue = []

    queue.append(source)
    while (queue):
        front = queue[0]
        queue.pop(0)

        if (front.x == target.x and front.y == target.y):
            return front.steps
        
        for i in range(8):
            nx = front.x + dx[i]
            ny = front.y + dy[i]

            appenend = str(nx) + ', ' + str(ny)

            if not appenend in visited and nx > 0 and ny > 0 and nx <= 8 and ny <= 8:
                nextNode = Node(nx, ny, front.steps + 1)
                queue.append(nextNode)
                visited.append(appenend)

s = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]

source = Node(s[0], s[1], 0)
target = Node(t[0], t[1], -1)

print(BFS(source, target))

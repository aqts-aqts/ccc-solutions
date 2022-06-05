import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)

class Person:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

m = int(input())
queue = [None]
q = int(input())
for _ in range(q): queue.append(Person(input().strip(), int(input())))

time = [sys.maxsize] * (q + 1)
group = [-1] * (q + 1)
time[0] = 0
group[0] = 0
for i in range(q + 1):
    j = 1
    c = 0
    while j <= m and i + j - 1 < q:
        c = max(c, queue[i + j].speed)
        if time[i] + c < time[i + j]:
            time[i + j] = time[i] + c
            group[i + j] = j
        j += 1
print('Total Time: ' + str(time[q]))

groups = [0] * (q + 1)
x = 0
while group[q] != 0:
    x += 1
    groups[x] = group[q]
    q -= group[q]

pointer = 0
for i in range(x, -1, -1):
    for j in range(groups[i]):
        pointer += 1
        print(queue[pointer].name, end=' ' if j < groups[i] - 1 else '\n')
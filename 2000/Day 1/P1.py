import sys
input = sys.stdin.readline
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
connections = [set() for _ in range(26)]

depth = set(); visited = set()   
def dfs(start):
    if start in lower:
        depth.add(start); return
    visited.add(start)
    for connection in connections[upper.index(start)]:
        if connection not in visited: dfs(connection)

references = []
for i in range(n):
    inequality = input().split()
    references.append(upper.index(inequality[0]))
    if inequality[2] in upper: references.append(upper.index(inequality[2]))
    connections[upper.index(inequality[0])].add(inequality[2])

for i in range(26):
    if i not in references: continue
    for c in connections[i].copy():
        if c in upper:
            connections[i].remove(c)
            dfs(c)
            connections[i] |= depth
            depth = set(); visited = set()

for i in range(26):
    if i not in references: continue
    subset = sorted(list(connections[i]))
    print(upper[i] + ' = {',end=''); print(*subset, sep=',',end=''); print('}')

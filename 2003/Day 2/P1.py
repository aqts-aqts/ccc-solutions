from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
constraints = []
s = 0
for i in range(k):
    constraints.append(list(map(int, input().split())))
for perm in permutations([i + 1 for i in range(n)]):
    satisfy = True
    for c in constraints:
        if perm.index(c[0]) >= perm.index(c[1]):
            satisfy = False
    if satisfy:
        s += 1
print(s)
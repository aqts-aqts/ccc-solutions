from collections import deque

r = int(input())
c = int(input())

n = r * c

v = [list() for _ in range(n)]
for i in range(1, r + 1):
    row = list(map(int, input().split()))
    for j in range(1, c + 1):
        v[i * j - 1].append(row[j - 1])

stack = deque()
visited = set()
stack.append(v[0][0])

done = False

while stack:
    cur = stack.pop()

    if cur == n:
        print('yes')
        done = True
        break

    if cur < n and cur - 1 not in visited:
        visited.add(cur - 1)
        for i in v[cur - 1]:
            if i <= n:
                stack.append(i)

if not done:
    print('no')
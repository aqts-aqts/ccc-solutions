import sys
input = sys.stdin.readline

rows = [0] * int(input())
columns = [0] * int(input())
actions = int(input())

for i in range(actions):
    a = input().split()
    if a[0] == 'R':
        rows[int(a[1]) - 1] += 1
    else:
        columns[int(a[1]) - 1] += 1

count = 0
for r in rows:
    for c in columns:
        if (r + c) % 2 != 0:
            count += 1

print(count)

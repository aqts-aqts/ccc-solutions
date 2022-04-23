from collections import defaultdict

x = int(input())
friends = defaultdict(list)
enemies = defaultdict(list)
groups = []
for v in range(x):
    s1, s2 = input().split()
    friends[s1].append(s2)

y = int(input())
for v in range(y):
    s1, s2 = input().split()
    enemies[s1].append(s2)

g = int(input())
for i in range(g):
    groups.append(input().split())

violations = 0
for group in groups:
    for student in group:
        for friend in friends[student]:
            if friend not in group:
                violations += 1
        for enemy in enemies[student]:
            if enemy in group:
                violations += 1
print(violations)
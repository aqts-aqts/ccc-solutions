t = int(input())
c = int(input())

tasks = []
for i in range(c):
    tasks.append(int(input()))

time = 0
chores = 0
while time < t:
    small = min(tasks)
    if time + small <= t:
        time += small
        tasks.remove(small)
        chores += 1
    else:
        break
print(chores)
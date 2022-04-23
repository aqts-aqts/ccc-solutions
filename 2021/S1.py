a = int(input())
sides = input().split()
for s in range(len(sides)):
    sides[s] = int(sides[s])
widths = input().split()
for w in range(len(widths)):
    widths[w] = int(widths[w])

num = 0
current = [0,1]
for i in range(a):
    num += widths[i] * (sides[current[0]] + sides[current[1]]) / 2
    current[0] += 1
    current[1] += 1

print(num)
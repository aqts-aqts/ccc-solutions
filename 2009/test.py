x = int(input())
b = []
for i in range(x):
    b.append(int(''.join(input().split()), 2))

for i in range(6):
    y = int(''.join(input().split()), 2)
    c = [y]
    for i in range(len(b)):
        c.append(b[i] ^ y)
    print(c)
    b = c.copy()
n = int(input())

mainst = {}
moves = []

for _ in range(n):
    name, f, t = input().split()
    f, t = int(f), int(t)
    mainst[f] = name
    moves.append((name, f, t))

order = []
for _ in range(n):
    i = 0
    while i < len(moves):
        name = moves[i][0]
        if not moves[i][2] in mainst:
            mainst[moves[i][2]] = name
            mainst.pop(moves[i][1])
            moves.pop(i)
            order.append(name)
        else:
            i += 1

if len(order) < n:
    print("Impossible")
else:
    print('\n'.join(order))
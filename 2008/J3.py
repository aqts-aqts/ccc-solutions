keypad = ['abcdef',
          'ghijkl',
          'mnopqr',
          'stuvwx',
          'yz -.!']

def inlist(e, l):
    for c in l:
        for p in c:
            if p == e:
                toreturn = [l.index(c),c.index(e)]
                return toreturn
    return -1

moves = 0
pos = [0,0]
totype = input().lower() + '!'
for c in totype:
    cpos = inlist(c, keypad)
    while keypad[pos[0]][pos[1]] != c:
        if pos[0] < cpos[0]:
            moves += 1
            pos[0] += 1
            continue
        elif pos[0] > cpos[0]:
            moves += 1
            pos[0] -= 1
            continue

        if pos[1] < cpos[1]:
            moves += 1
            pos[1] += 1
            continue
        elif pos[1] > cpos[1]:
            moves += 1
            pos[1] -= 1
            continue


print(moves)

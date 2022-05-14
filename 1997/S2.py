import sys
input = sys.stdin.readline

def fp(n):
    pairs = []    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: pairs.append([i, n // i])
    return pairs

for _ in range(int(input())):
    n = int(input())
    pairs = fp(n)
    nasty = False
    for pair1 in pairs:
        for pair2 in pairs:
            if pair1 == pair2: continue
            if pair1[1] - pair1[0] == sum(pair2): nasty = True; break
    print(n, end=' ')
    if nasty: print('is nasty')
    else: print('is not nasty')
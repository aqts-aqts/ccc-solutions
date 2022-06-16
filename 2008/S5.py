import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
moves = [[2, 1, 0, 2], [1, 1, 1, 1], [0, 0, 2, 1], [0, 3, 0, 0], [1, 0, 0, 1]]

dp = {}
def nukit(a, b, c, d, turn):
    if (a, b, c, d, turn) in dp: return dp[(a, b, c, d, turn)]
    if turn:
        for move in moves:
            if a - move[0] < 0 or b - move[1] < 0 or c - move[2] < 0 or d - move[3] < 0: continue
            dp[(a, b, c, d, turn)] = nukit(a - move[0], b - move[1], c - move[2], d - move[3], False)
            if dp[(a, b, c, d, turn)]: return True
        return False
    else:
        for move in moves:
            if a - move[0] < 0 or b - move[1] < 0 or c - move[2] < 0 or d - move[3] < 0: continue
            dp[(a, b, c, d, turn)] = nukit(a - move[0], b - move[1], c - move[2], d - move[3], True)
            if not dp[(a, b, c, d, turn)]: return False
        return True

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    perfect = nukit(a, b, c, d, True)
    if perfect: print('Patrick')
    else: print('Roland')
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, x, y, moves):
        self.x = x
        self.y = y
        self.moves = moves

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def solve(r, c, pr, pc, kr, kc):
    dp = [sys.maxsize] * (r + 1)
    visited = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    queue = [Node(kc, kr, 0)]
    visited[kr][kc] = 1
    while queue:
        cur = queue.pop(0)
        if cur.x == pc: dp[cur.y] = cur.moves
        for i in range(8):
            nx = cur.x + dx[i]
            ny = cur.y + dy[i]
            try: 
                if not visited[ny][nx] and nx <= c and ny <= r and nx > 0 and ny > 0:
                    visited[ny][nx] = 1
                    queue.append(Node(nx, ny, cur.moves + 1))
            except: pass
    for i in range(pr + 1, r + 1):
        if dp[i] == i - pr: return 'Win in ' + str(dp[i]) + ' knight move(s).'
    for i in range(pr, r):
        if dp[i + 1] == i - pr: return 'Stalemate in ' + str(dp[i + 1]) + ' knight move(s).'
    for i in range(pr + 1, r):
        if i - pr > dp[i] and dp[i] % 2 == (i - pr) % 2: return 'Win in ' + str(i - pr) + ' knight move(s).'
    for i in range(pr, r - 1):
        if i - pr > dp[i + 1] and dp[i + 1] % 2 == (i - pr) % 2: return 'Stalemate in ' + str(i - pr) + ' knight move(s).'
    return 'Loss in ' + str(r - pr - 1) + ' knight move(s).'

for _ in range(int(input())):
    r = int(input()); c = int(input())
    pr = int(input()); pc = int(input())
    kr = int(input()); kc = int(input())
    print(solve(r, c, pr, pc, kr, kc))
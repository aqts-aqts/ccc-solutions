import sys
input = sys.stdin.readline

def solve(paths, n):
    dp = [1 if i in paths[n] else 0 for i in range(n + 1)]
    for i in range(n - 1, 0, -1):
        while len(paths[i]) > 0: dp[paths[i].pop()] += dp[i]
    print(dp[1])

n = int(input())
paths = [set() for _ in range(n + 1)]
x, y = map(int, input().split())
while x != 0:
    paths[x].add(y)
    paths[y].add(x)
    x, y = map(int, input().split())
solve(paths, n)
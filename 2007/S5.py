import sys
input = sys.stdin.readline

def solve(pins, k, w, n):
    global dp
    if k == 0 or n < w - 1: return 0
    if dp[n] is not None: return dp[n]
    pSum = sum(pins[n - i] for i in range(w))
    dp[n] = max(pSum + solve(pins, k - 1, w, n - w), solve(pins, k, w, n - 1))
    return dp[n]

for case in range(int(input())):
    n, k, w = map(int, input().split())
    pins = [int(input()) for _ in range(n)]
    dp = [None] * n
    print('Result: ', solve(pins, k, w, n - 1))
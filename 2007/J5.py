from bisect import insort_left, bisect_left, bisect_right
import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)

min = int(input())
max = int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
n = int(input())
for _ in range(n): insort_left(motels, int(input()))

dp = [0] * len(motels)
def solve(n):
    left = bisect_left(motels, motels[n] - max)
    right = bisect_right(motels, motels[n] - min)
    for i in range(left, right):
        dp[i] += 1
        solve(i)
solve(len(motels) - 1)
print(dp[0])

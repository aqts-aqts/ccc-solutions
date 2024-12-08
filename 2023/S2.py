import sys

n = int(input())
heights = list(map(int, input().split()))

dp = {} # Let dp[i][j] be the most symmetric crop at i with a length of j
min_symmetrys = [sys.maxsize] * (n + 1) # Let min_symmetrys[i] be the minimum symmetry of a crop with a length of i
min_symmetrys[0] = 0
min_symmetrys[1] = 0

# Fill out dp array for lengths 1 and 2
for i in range(n):
    dp[(i, 1)] = 0
    if i < n - 1:
        dp[(i, 2)] = abs(heights[i] - heights[i + 1])
        min_symmetrys[2] = min(min_symmetrys[2], dp[(i, 2)])

# Fill out dp array for lengths 3 and above
for j in range(3, n + 1):
    for i in range(n - j + 1):
        dp[(i, j)] = dp[(i + 1, j - 2)] + abs(heights[i] - heights[i + j - 1])
        min_symmetrys[j] = min(min_symmetrys[j], dp[(i, j)])

print(' '.join(map(str, min_symmetrys[1:])))
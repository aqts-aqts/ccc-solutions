# Greedy method + dynamic programming
# Max time complexity: O(nm^2)

# dp[i][j][k] = max value of pies with pies[i:] and extras[j:k]

# Observation 1: There are four operations that can be done each time:
# 1. Skip the next pie (solve(i + 1, j, k))
# 2. Take the current pie and skip next (cur + solve(i + 2, j, k))
# 3. Insert the smallest pie to take both pies (cur + solve(i + 1, j + 1, k))
# 4. Insert the smallest and largest pie consecutively to take largest pie in `extras` (cur + extras[k] + solve(i + 2, j + 1, k - 1))

# Submission 1: AC cases 1-5, WA cases 6-10, TLE cases 11-14, AC case 15
# Is the greedy method correct? Do we always rule out the smallest pie in `extras` for the maximal result?
# Is the dynamic programming correct? What if we want to add more than two pies from `extras`?

# Observation 2: Adding three pies from `extras` can be optimal (cur + extras[k] + solve(i + 1, j + 2, k - 1))
# We add an extra minimal pie to be able to take the next pie in `pies` and the largest pie in `extras`

import sys
sys.setrecursionlimit(1000000)

n = int(input())
pies = list(map(int, (input() for _ in range(n))))

m = int(input())
extras = list(map(int, (input() for _ in range(m))))

extras = sorted(extras)

dp = [[[0 for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

def solve(i, j, k):
    if i >= n:
        return 0
    if dp[i][j][k]:
        return dp[i][j][k]
    
    cur = pies[i]

    if j < k:
        dp[i][j][k] = max(solve(i + 1, j, k), cur + solve(i + 1, j + 1, k), cur + solve(i + 2, j, k), extras[k] + solve(i, j + 1, k - 1))
    elif j == k:
        dp[i][j][k] = max(solve(i + 1, j, k), cur + solve(i + 1, j + 1, k), cur + solve(i + 2, j, k))
    else:
        dp[i][j][k] = max(solve(i + 1, j, k), cur + solve(i + 2, j, k))

    return dp[i][j][k]

print(solve(0, 0, m - 1))
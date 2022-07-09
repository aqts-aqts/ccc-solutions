import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)

n = int(input())
rice = list(map(int, input().split()))

dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
sum = [0] * (n + 2)
result = 0
for i in range(n):
    dp[i][i] = rice[i]
    result = max(result, dp[i][i])
    if not i: sum[0] = dp[i][i]
    else: sum[i] = sum[i - 1] + dp[i][i]

for length in range(1, n):
    for i in range(n - length):
        pos = length + i
        left = i + 1
        right = pos
        while left <= right:
            if dp[i][left - 1] and dp[i][left - 1] == dp[right][pos] and (left == right or dp[left][right - 1]):
                dp[i][pos] = max(dp[i][pos], dp[i][left - 1] + dp[left][right - 1] + dp[right][pos])
                result = max(result, dp[i][pos])
                break
            if sum[left - 1] - sum[i - 1] < sum[pos] - sum[right - 1]: left += 1
            else: right -= 1
print(result)
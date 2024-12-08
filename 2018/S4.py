# For n = 1e9
# From 500,000,001 to 1,000,000,000: n // k is always 1
# From 333,333,334 to 500,000,000: n // k is always 2
# From 250,000,001 to 333,333,333: n // k is always 3
# From 200,000,001 to 250,000,000: n // k is always 4
# From 166,666,667 to 200,000,000: n // k is always 5
# From 142,857,143 to 166,666,666: n // k is always 6
# From 125,000,001 to 142,857,142: n // k is always 7
# From 111,111,112 to 125,000,000: n // k is always 8
# From 100,000,001 to 111,111,111: n // k is always 9
# From 90,909,092 to 100,000,000: n // k is always 10
# From 83,333,334 to 90,909,091: n // k is always 11
# From 76,923,077 to 83,333,333: n // k is always 12
# From 71,428,572 to 76,923,076: n // k is always 13
# From 66,666,668 to 71,428,571: n // k is always 14
# From 62,500,002 to 66,666,667: n // k is always 15
# From 58,823,530 to 62,500,001: n // k is always 16
# From 55,555,556 to 58,823,529: n // k is always 17
# From 52,631,579 to 55,555,555: n // k is always 18
# From 50,000,002 to 52,631,578: n // k is always 19
# From 47,619,048 to 50,000,001: n // k is always 20
# From 45,454,546 to 47,619,047: n // k is always 21
# From 43,478,261 to 45,454,545: n // k is always 22
# ...
# From 2,000,001 to 2,004,008: n // k is always 499
# From 49,998 to 50,000: n // k is always 20000
# Smaller than sqrt(n), all n // k are different
# This is always at most 2 * sqrt(n) numbers to check
# Instead of checking every single k, we can check every k UP TO sqrt(n), and then check every n // k

from math import sqrt

n = int(input())
dp = {}
dp[1] = 1
dp[2] = 1

def solve(n):
    if n in dp: return dp[n]

    dp[n] = 0

    for x in range(1, int(sqrt(n)) + 1):
        dp[n] += solve(x) * (n // x - n // (x + 1))
    
    end = int(sqrt(n))
    if int(sqrt(n)) == n // int(sqrt(n)):
        end -= 1
    
    for k in range(end, 1, -1):
        dp[n] += solve(n // k)
    return dp[n]

print(solve(n))
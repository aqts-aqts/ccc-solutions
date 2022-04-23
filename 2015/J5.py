n = int(input())
k = int(input())

pi = dict()

def findCombinations(n, k):
    if n < k:
        return 0
    if n == k or k == 1:
        return 1
    if (n, k) in pi:
        return pi[(n, k)]
    pi[(n, k)] = findCombinations(n - 1, k - 1) + findCombinations(n - k, k)
    return pi[(n, k)]

print(findCombinations(n, k))

import sys
input = sys.stdin.readline

def solve(n1, n2, s, layer, nums):
    global solution
    if layer == min(len(n1), len(n2)): solution = nums
    for i in range(10):
        if i == 0 and layer == len(n1) - 1: continue
        if nums[i] == None or nums[i] == n1[layer]: nums[i] = n1[layer]
        else: continue
        for j in range(10):
            if j == 0 and layer == len(n2) - 1: continue
            if nums[j] == None or nums[j] == n2[layer]: nums[j] = n2[layer]
            else: continue
            if nums[(i + j) % 10] == s[layer] or nums[(i + j) % 10] == None:
                nums[(i + j) % 10] = s[layer]
                solve(n1, n2, s, layer + 1, nums)

for _ in range(int(input())):
    solution = [None] * 10
    n1 = input().strip(); n2 = input().strip(); s = input().strip()
    solve(n1, n2, s, 0, [None] * 10)
    for i in range(len(solution)):
        ss = solution[i]
        if ss != None: n1 = n1.replace(ss, s); n2 = n2.replace(ss, s); s.replace(ss, s)
    print(n1, n2, s, sep='\n')
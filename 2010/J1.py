n = int(input())
p = []
for i in range(1, 6):
    if n-i <=5 and i <= n:
        if ([n-i, i] not in p):
            p.append([i, n-i])
print(len(p))
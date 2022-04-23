num = int(input())
partner1 = input().split()
partner2 = input().split()

pairs = []
perfect = True
for p in range(num):
    p1 = partner1[p]
    p2 = partner2[p] 

    if p1 == p2:
        perfect = False
        break
    
    if ([p1, p2] or [p2, p1]) not in pairs or p == 0:
        for pair in pairs:
            if pair[0] == p1 and pair[1] != p2 or pair[0] != p1 and pair[1] == p2 or pair[0] == p2 and pair[1] != p1 or pair[0] != p2 and pair[1] == p1:
                perfect = False
                break
        pairs.append([p1, p2])

    if not perfect:
        break

if perfect:
    print('good')
else:
    print('bad')
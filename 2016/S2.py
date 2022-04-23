t = int(input())
if t == 1:
    t = True
else:
    t = False

n = int(input())
dmoj = [int(x) for x in input().split()]
peg = [int(x) for x in input().split()]

s = []
if t:
    for i in range(n):
        s.append(max(max(dmoj), max(peg)))
        dmoj.remove(max(dmoj))
        peg.remove(max(peg))
elif not t:
    for i in range(n):
        s.append(max(max(dmoj), min(peg)))
        dmoj.remove(max(dmoj))
        peg.remove(min(peg))

print(sum(s))

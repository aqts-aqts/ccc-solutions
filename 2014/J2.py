ignore = int(input())
votes = input()
av = 0
bv = 0
for v in votes:
    if v == 'A':
        av += 1
    else:
        bv += 1

if av == bv:
    print("Tie")
elif av > bv:
    print("A")
else:
    print("B")
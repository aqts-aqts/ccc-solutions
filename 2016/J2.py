l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l3 = [int(x) for x in input().split()]
l4 = [int(x) for x in input().split()]
c1 = [l1[0], l2[0], l3[0], l4[0]]
c2 = [l1[1], l2[1], l3[1], l4[1]]
c3 = [l1[2], l2[2], l3[2], l4[2]]
c4 = [l1[3], l2[3], l3[3], l4[3]]

if sum(l1) == sum(l2) == sum(l3) == sum(l4) == sum(c1) == sum(c2) == sum(c3) == sum(c4):
    print("magic")
else:
    print("not magic")
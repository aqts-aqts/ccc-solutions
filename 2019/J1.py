a3s = int(input())
a2s = int(input())
a1s = int(input())
b3s = int(input())
b2s = int(input())
b1s = int(input())

if a3s*3+a2s*2+a1s > b3s*3+b2s*2+b1s:
    print("A")
elif b3s*3+b2s*2+b1s > a3s*3+a2s*2+a1s:
    print("B")
else:
    print("T")

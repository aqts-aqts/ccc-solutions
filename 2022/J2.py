n=int(input())
p=0
for i in range(n):
    pts=int(input())
    fouls=int(input())
    stars=pts*5-fouls*3
    if stars>40:
        p+=1
print(p,end="")
if p==n:
    print("+")
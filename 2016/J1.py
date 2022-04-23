a=input()
aa=input()
ab=input()
ac=input()
ad=input()
ae=input()
c=0
g = [a,aa,ab,ac,ad,ae]
for ag in g:
    if ag == 'W':
        c+=1
if c==5 or c==6:
    print(1)
elif c==3 or c==4:
    print(2)
elif c==2 or c==1:
    print(3)
else:
    print(-1)
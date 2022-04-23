n = int(input())
line1=input()
line2=input()
c=0
for i in range(n):
    if line1[i] == 'C' and line2[i] == 'C':
        c+=1
print(c)
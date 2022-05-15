no='ABCDEFGJKLMPQRTUVWY'
a=input()
for i in range(len(a)):
    if a[i] in no: print('NO'); break
    if i==len(a)-1:print('YES')
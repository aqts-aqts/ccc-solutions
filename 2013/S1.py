def isdistinct(y):
    return len(set(str(y))) == len(str(y))

year=int(input())
while True:
    year+=1
    if isdistinct(year): print(year);break
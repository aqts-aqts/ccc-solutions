k = int(input())
nums=[]
for i in range(k):
    n=int(input())
    if n==0:
        nums.pop(-1)
    else:
        nums.append(n)
print(sum(nums))
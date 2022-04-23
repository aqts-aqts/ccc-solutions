num = int(input())
times=int(input())
count=0
count+=num
for i in range(times):
    num*=10
    count+=num
print(count)

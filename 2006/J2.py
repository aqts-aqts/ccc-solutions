ways=0
a=int(input())
b=int(input())
for i in range(1, a+ 1):
    for j in range(1,b+1):
        if i+j==10:
            ways+=1

if ways==0:
    print("There are 0 ways to get the sum 10.")
elif ways==1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are " + str(ways) + " ways to get the sum 10.")

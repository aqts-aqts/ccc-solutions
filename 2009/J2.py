import sys
input = sys.stdin.readline
t=int(input())
p=int(input())
i=int(input())
pts = int(input())

def solve(bt,np,yp,visited=dict()):
    if (bt,np,yp) in visited:
        return 0
    if bt*t+np*p+yp*i < pts:
        if bt+np+yp > 0:
            print(str(bt) + ' Brown Trout, ' + str(np) + ' Northern Pike, ' + str(yp) + ' Yellow Pickerel')
            visited[(bt,np,yp)] = 1
            return solve(bt+1,np,yp)+solve(bt,np+1,yp)+solve(bt,np,yp+1)+1
        else:
            return solve(bt+1,np,yp)+solve(bt,np+1,yp)+solve(bt,np,yp+1)
    if bt*t+np*p+yp*i > pts:
        visited[(bt,np,yp)] = 0
        return 0
    else:
        print(str(bt) + ' Brown Trout, ' + str(np) + ' Northern Pike, ' + str(yp) + ' Yellow Pickerel')
        visited[(bt,np,yp)] = 1
        return 1

print('Number of ways to catch fish: ' + str(solve(0,0,0)))
import sys
input = sys.stdin.readline
p = int(input())
g = int(input())
r = int(input())
o = int(input())
amnt = int(input())

minsum=sys.maxsize
def solve(ps,gs,rs,os,visited=dict()):
    global minsum
    if (ps,gs,rs,os) in visited:
        return 0
    if ps*p+gs*g+rs*r+os*o < amnt:
        return solve(ps+1,gs,rs,os)+solve(ps,gs+1,rs,os)+solve(ps,gs,rs+1,os)+solve(ps,gs,rs,os+1)
    if ps*p+gs*g+rs*r+os*o > amnt:
        visited[(ps,gs,rs,os)] = 0
        return 0
    else:
        if ps+gs+rs+os < minsum:
            minsum=ps+gs+rs+os
        print('# of PINK is ' + str(ps) + ' # of GREEN is ' + str(gs) + ' # of RED is ' + str(rs) + ' # of ORANGE is ' + str(os))
        visited[(ps,gs,rs,os)] = 1
        return 1

print('Total combinations is ' + str(solve(0,0,0,0)) + '.')
print('Minimum number of tickets to print is ' + str(minsum) + '.')
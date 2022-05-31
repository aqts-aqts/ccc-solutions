import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
square = 1
while square < 100:
    move = int(input())
    if move == 0: print('You Quit!'); break
    if square + move <= 100: square += move
    if square == 9: square = 34
    if square == 40: square = 64
    if square == 67: square = 86
    if square == 54: square = 19
    if square == 90: square = 48
    if square == 99: square = 77
    print('You are now on square ' + str(square))
    if square == 100: break
    
if square == 100: print('You Win!')
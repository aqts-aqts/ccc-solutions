import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
vowels = 'aeiouAEIOU'
n = int(input())
for _ in range(n):
    syllable = ['','','','']
    for i in range(4):
        verse = input().split()
        last = list(reversed(verse[-1]))
        p = -1
        for c in range(len(last)): 
            if last[c] in vowels: p = c; break
        if p >= 0:
            syllable[i] = ''.join(reversed(last[:p + 1])).lower()
        else:
            syllable[i] = verse[-1].lower()
    if syllable[0] == syllable[1] == syllable[2] == syllable[3]: print('perfect')
    elif syllable[0] == syllable[1] and syllable[2] == syllable[3]: print('even')
    elif syllable[0] == syllable[2] and syllable[1] == syllable[3]: print('cross')
    elif syllable[0] == syllable[3] and syllable[1] ==syllable[2]: print('shell')
    else: print('free')
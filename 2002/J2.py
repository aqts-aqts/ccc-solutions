import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
vowel = 'aeiouy'

word = input().strip()
while word != 'quit!':
    if len(word) > 4 and word[-2] == 'o' and word[-1] == 'r' and word[-3] not in vowel:
        word = word.replace('or', 'our')
        print(word)
    else: print(word)
    word = input().strip()
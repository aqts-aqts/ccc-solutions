import sys
input = sys.stdin.readline

line = input()
happy = line.count(':-)')
sad = line.count(':-(')
if happy > sad: print('happy')
elif happy == 0 and sad == 0: print('none')
elif happy == sad: print('unsure')
else: print('sad')
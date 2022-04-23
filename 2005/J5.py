word = input().strip()
while word != 'X':
    for i in range(len(word)): word = word.replace('BAS', 'A'); word = word.replace('ANA', 'A')
    if word == 'A': print("YES"); word = input().strip()
    else: print("NO"); word = input().strip()
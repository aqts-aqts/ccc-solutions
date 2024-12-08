keys = input()
display = input()

frequency = {}
silly = ''
silly_frequency = 0

for key in keys:
    if key in frequency:
        frequency[key] += 1
    else:
        frequency[key] = 1

for letter in display:
    if letter in frequency:
        frequency[letter] -= 1
    elif letter not in frequency:
        silly = letter
        silly_frequency += 1
    if letter in frequency and frequency[letter] == 0:
        frequency.pop(letter)

n = len(keys)
first = list(frequency)[0]
second = list(frequency)[1] if len(frequency) == 2 else None
if len(frequency) == 1:
    print(f'{first} {silly}')
    print('-')
else:
    possibility = keys.replace(first, silly)
    possibility = possibility.replace(second, '')
    if possibility == display:
        print(f'{first} {silly}')
        print(second)
    else:
        print(f'{second} {silly}')
        print(first)
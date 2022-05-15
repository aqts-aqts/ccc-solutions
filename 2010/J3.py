action = input()
v = {'A': 0, 'B': 0}
while action != '7':
    vals = action.split()
    if vals[0] == '1':
        v[vals[1]] = int(vals[2])
    elif vals[0] == '2':
        print(v[vals[1]])
    elif vals[0] == '3':
        v[vals[1]] += v[vals[2]]
    elif vals[0] == '4':
        v[vals[1]] *= v[vals[2]]
    elif vals[0] == '5':
        v[vals[1]] -= v[vals[2]]
    elif vals[0] == '6':
        v[vals[1]] //= v[vals[2]]
    action = input()
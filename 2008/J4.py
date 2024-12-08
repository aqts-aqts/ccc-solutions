prefix = input().split()[::-1]

while not(len(prefix) == 1 and prefix[0] == '0'):
    expressions = []
    operators = []

    i = 0
    while prefix:
        token = prefix.pop()
        if token.isdigit():
            expressions.append((token, i))
        else:
            operators.append((token, i))

        while len(expressions) >= 2 and len(operators) >= 1 and expressions[-1][1] > expressions[-2][1] > operators[-1][1]:
            j = min(expressions[-1][1], expressions[-2][1])
            x, y = expressions.pop(), expressions.pop()
            expressions.append((min(x, y, key=lambda k: k[1])[0] + ' ' + max(x, y, key=lambda k: k[1])[0] + ' ' + operators.pop()[0], j))
        i += 1
    
    print(expressions[0][0])
    prefix = input().split()[::-1]
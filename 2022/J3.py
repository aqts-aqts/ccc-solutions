alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
actions='+-'
a=input()
num=False
for c in a:
    if c in alphabet:
        if num:
            print()
            num=False
        print(c,end="")
    elif c in actions:
        if c=='+':
            print(' tighten ',end="")
        else:
            print(' loosen ',end="")
    else:
        num=True
        print(c, end="")
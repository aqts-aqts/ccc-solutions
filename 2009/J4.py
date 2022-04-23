import math
w = int(input())
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
outputs = []

def addSpace(s, amnt):
    c = 6
    x = amnt
    while x > 0:
        if s.count('.') > 0:
            index = s.index('.')
            s = s.replace('.', '/', 1)
        else:
            index = s.index('/')
            s = s.replace('/', '|', 1)
        
        if math.ceil(amnt / c) <= x and not s.count('.') > 0:
            s = s[:index] + '|' * math.ceil(amnt / c) + s[index:]
            x -= math.ceil(amnt / c)
        else:
            s = s[:index] + '|' + s[index:]
            x -= 1
    return s

possibles = [
    ['WELCOME','TO..CCC','GOOD...','LUCK...','TODAY..'],
    ['WELCOME.','TO...CCC','GOOD....','LUCK....','TODAY...'],
    ['WELCOME..','TO....CCC','GOOD.LUCK','TODAY....'],
    ['WELCOME.TO','CCC...GOOD','LUCK.TODAY'],
    ['WELCOME..TO','CCC....GOOD','LUCK..TODAY'],
    ['WELCOME...TO','CCC.....GOOD','TODAY.......'],
    ['WELCOME....TO','CCC.GOOD.LUCK','TODAY........'],
    ['WELCOME.TO.CCC','GOOD......LUCK','TODAY.........'],
    ['WELCOME..TO.CCC','GOOD.LUCK.TODAY'],
    ['WELCOME..TO..CCC','GOOD..LUCK.TODAY'],
    ['WELCOME...TO..CCC','GOOD..LUCK..TODAY'],
    ['WELCOME...TO...CCC','GOOD...LUCK..TODAY'],
    ['WELCOME.TO.CCC.GOOD','LUCK..........TODAY'],
    ['WELCOME..TO.CCC.GOOD','LUCK...........TODAY'],
    ['WELCOME..TO..CCC.GOOD','LUCK............TODAY'],
    ['WELCOME..TO..CCC..GOOD','LUCK.............TODAY'],
    ['WELCOME...TO..CCC..GOOD','LUCK..............TODAY'],
    ['WELCOME.TO.CCC.GOOD.LUCK','TODAY...................'],
    ['WELCOME..TO.CCC.GOOD.LUCK','TODAY....................'],
    ['WELCOME..TO..CCC.GOOD.LUCK','TODAY....................'],
    ['WELCOME..TO..CCC..GOOD.LUCK','TODAY.....................'],
    ['WELCOME..TO..CCC..GOOD..LUCK','TODAY.....................'],
    ['WELCOME...TO..CCC..GOOD..LUCK','TODAY......................'],
    ['WELCOME.TO.CCC.GOOD.LUCK.TODAY']
]


if w > 30:
    print(addSpace(possibles[23][0], w - 30).replace('|','.').replace('/','.'))
else:
    for p in possibles[w - 7]:
        print(p)
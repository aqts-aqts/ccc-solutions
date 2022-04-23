class Section:
    def __init__(self):
        self.l = 0
        self.m = 0
        self.s = 0
    def add(self, book):
        if book == 'L':
            self.l += 1
        if book == 'S':
            self.s += 1
        if book == 'M':
            self.m += 1

books = input()
total = Section()

for book in books:
    total.add(book)

l = Section()
m = Section()
s = Section()

j = 0
for i in range(total.l):
    l.add(books[j])
    j += 1
for i in range(total.m):
    m.add(books[j])
    j += 1
for i in range(total.s):
    s.add(books[j])
    j += 1

print(l.m + l.s + m.l + m.s - min(m.l, l.m))

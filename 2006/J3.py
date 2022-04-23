t = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
a = input()

while a != "halt":
    total = 0
    for i in range(len(a)):
        for b in t:
            if a[i] in b:
                total += b.index(a[i]) + 1
                break
        if i < len(a)-1 and (a[i] == a[i+1] or a[i+1] in b):
            total += 2
    print(total)
    a = input()
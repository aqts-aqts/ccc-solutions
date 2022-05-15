for _ in range(int(input())):
    texts = []
    t = input().split()
    while t:
        texts.append(t)
        t = input().split()

    visited = dict()
    word = 0
    for i in range(len(texts)):
        for j in range(len(texts[i])):
            if texts[i][j] not in visited: visited[texts[i][j]] = str(word + 1); word += 1
            elif texts[i][j] in visited: texts[i][j] = visited[texts[i][j]]
        print(' '.join(texts[i]))
    print()
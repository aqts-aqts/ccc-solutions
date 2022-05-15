n = int(input())
for _ in range(n):
    s = int(input()); v = int(input()); o = int(input())
    subjects = []; verbs = []; objects = []
    for _ in range(s): subjects.append(input())
    for _ in range(v): verbs.append(input())
    for _ in range(o): objects.append(input())
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentences.append(subject + ' ' + verb + ' ' + obj + '.')
    sentences = sorted(sentences, key=str.lower)
    for sentence in sentences:
        print(sentence)
    print()
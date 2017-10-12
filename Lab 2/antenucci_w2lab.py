hail = open('TheVictors.txt')
counts = {}
for line in hail:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

wordlst = sorted(counts.items(), key = lambda x : x[0])
wordlst = sorted(counts.items(), key = lambda x : x[1], reverse = True)
for key,val in wordlst[:15]:
    print(key, val)

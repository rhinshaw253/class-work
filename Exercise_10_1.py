mydict = {}
mytups = []
fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    if not len(words) < 3 and words[0] == "From" :
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1

list = list()
for key, val in counts.items():
    list.append( (val, key)  ) 

for key, val in list[:10]: 

    print(key, val)

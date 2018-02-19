fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand: 
    words = line.split()
    if len(words) < 3: continue
    if words[0] != "From": continue
    if words[1] not in counts.keys():
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1
print(counts) 
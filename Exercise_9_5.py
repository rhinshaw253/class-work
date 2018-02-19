fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand: 
    words = line.split()
    if len(words) < 3: continue
    if words[0] != "From": continue
    find = words[1].find("@")
    address = words[1][find+1:]
    if address not in counts:
        counts[address] = 1
    else:
        counts[address] += 1
print(counts) 
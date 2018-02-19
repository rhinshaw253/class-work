fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand: 
    words = line.split()
    if not len(words) == 0: continue
    if words[0] != "From" : continue
    time = words[5].split(":")[0]
    if time not in counts.keys():
        counts(time) = 1
    else:
        counts[time] += 1
        
list = list()
for key, val in counts.items():
    list.append( (val, key)  ) 

for key, val in list : 
    print(key, val)

    
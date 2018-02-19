fname = "mbox-short.txt"
fhand = open(fname)
count = 0

for line in fhand:
    words = line.split()
    if not len(words) == 0 and words[0] == "From" : 
        print(words[1])
        count = count + 1
print(count) 
fname = "romeo.txt"
fhand = open(fname)
wordlist = []

for line in fhand:
    words = line.split()
    for x in words:
        if x in wordlist: continue
        wordlist.append(x)

wordlist.sort        
print(wordlist) 
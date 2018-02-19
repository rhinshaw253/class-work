dict = {}
fname = "words.txt"
fhand = open(fname)

for word in fhand:
    if word not in dict.keys():
        pair = word.rstrip()
        dict[pair] = pair
        
print(dict) 
def chop(c):
    del c[len(c)-1]
    del c[0]
    
numlist = [1, 2, 3, 4, 5]
chop(numlist)
print(numlist) 
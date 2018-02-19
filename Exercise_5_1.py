
total = 0 
count = 0
while True: 
    num = raw_input('Enter number: ')
    if num == 'done':
        break
    else:
        try:
            num = int(num)
            total = total + num
            count = count + 1
        except:
            print ('bad data')
            
print (total, count, float(total) / count)
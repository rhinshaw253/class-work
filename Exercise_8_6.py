list = []
while True:
    num = input("Enter a number: ") 
    if num == "done" :
        break
    try: 
        num= float(num)
    except: 
        print("Please enter a number or done when you are finished") 
        continue
    list.append(num)
    
print(list) 
print ("Maximum:", max(num))
print ("Minimum:", min(num))

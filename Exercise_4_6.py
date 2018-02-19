

full_hours = 40 
try: 
    hours = input('Enter your hours worked: ')
    hours = float(hours) 
    rate = input('Enter your hourly pay rate: ') 
    rate = float(rate) 
    if hours > full_hours: 
        total = ((hours - full_hours) * .5 * rate) + (hours * rate) 
    else:
        total = hours * rate
    print(total)  
except:
    print('Error, please enter numeric input') 
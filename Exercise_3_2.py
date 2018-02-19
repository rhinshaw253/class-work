
std_hours = 40 

try:
    hours_input = int(input("How many hours did you work?"))
    rate_input = int(input("What is your hourly rate?"))
    if hours_input > std_hours:
        total = ((hours_input - std_hours) * .5 * rate_input) + (hours_input * rate_input)
    else: 
        total = hours_input * rate_input 
    print (total)
except: 
    print("Error, please enter numeric input") 
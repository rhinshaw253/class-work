hours_input = int(input("How many hours did you work?"))
rate_input = int(input("What is your hourly rate?"))

std_hours = 40 

if hours_input > std_hours:
    total = ((hours_input - std_hours) * .5 * rate_input) + (hours_input * rate_input)
else: 
    total = hours_input * rate_input 

print (total)

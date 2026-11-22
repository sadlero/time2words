import time
from num2words import num2words as n2w

def h2w(hours): #h2w = hours to words
    hours = hours % 12 #converts 13:00 to 1:00
    if hours == 0:
        hours = 12 #makes sure 00:05 is read as twelve oh five
        
    return n2w(hours)

def m2w(minutes): #m2w = minutes to words
    if minutes == 0:
        return "o'clock"
    elif minutes in range(1, 10): 
        return f"oh {n2w(minutes)}" #ex 1:05 is one oh five
        
    return n2w(minutes)

def quarters(minutes):
    if minutes == 15:
        return "a quarter past"
    elif minutes == 30:
        return "half past"
    elif minutes == 45:
        return "a quarter to"

current_time = time.strftime("%H:%M")
hours, minutes = current_time.split(":")

hours = int(hours)
minutes = int(minutes)

def t2w(hours, minutes): #t2w = time to words
    if minutes == 0 and hours == 0:
        return "It's midnight."
    elif minutes == 15 or minutes == 30:
    	return(f"The time is {quarters(minutes)} {h2w(hours)}.") #the time is a quarter/half past hours
    elif minutes == 45:
    	hours = hours + 1
    	return(f"The time is {quarters(minutes)} {h2w(hours)}.") #the time is a quarter to hours+1
    elif minutes/11 == hours or minutes == 11 and hours == 11:  #all the digits are the same, wishing time!
        return (f"The time is {h2w(hours)} {m2w(minutes)}. Make a wish!") 
    else:
        return(f"The time is {h2w(hours)} {m2w(minutes)}.") #the time is hours minutes

print(t2w(hours, minutes))


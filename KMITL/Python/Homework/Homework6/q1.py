def time24hourTo12hour(x):
    y = x.split(":")
    hour = int(y[0])
    minute = int(y[1])
    if hour < 25:
        if 0 <= hour <= 11:
            print(f"{hour}:{minute} AM")
        if 13 <= hour <= 23:
            formathour = hour - 12
            print(f"{formathour}:{minute} PM")
        if hour == 12:
            print(f"{hour}:{minute} PM")    
    else:
        print("I dont know")
        
         
    
time24hourTo12hour("13:24")
    
    

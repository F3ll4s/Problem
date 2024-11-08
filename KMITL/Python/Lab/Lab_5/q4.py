for x in range(50,0,-1):
    if x % 3 == 0 or x % 5 == 0:
        continue
    else:
        if x == 1:
            print(x,end=".")
        else:
            print(x, end=",")
            continue
    

        
    
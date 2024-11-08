def list_number(x,y):
    if len(y) == 0:
        return False
    elif x == y[0]:
        return True
    else:
        return list_number(x,y[1:])
        
number = (2,[0,1,2,3])
print(list_number(*number))
print(number)
def list_reverse(x,y=[]):
    if len(x) == 0:
        return y
    elif len(x)-1 == 0:
        y.append(x[0])
        return y
    else:
        y.append(x[len(x)-1])
        x.pop(len(x)-1)
        return list_reverse(x,y)
    
print(list_reverse([1,2,3,4]))
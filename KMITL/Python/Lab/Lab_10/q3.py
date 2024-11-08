list1 = [3,1,1,1,7]
list2 = [4,1,1,2,2,5]

def get_the_difference(x,y):
    list3 =[]
    for a in range(len(x)):
        if x[a] not in y:
            list3.append(x[a])
    for b in range(len(y)):
        if y[b] not in x:
            list3.append(y[b])
            
    print(list3)
    
                
get_the_difference(list1,list2)
list1 = [1,5,16,61,111]
list2 = [2,4,5,6]

def merge(x,y):
    new_list = []
    a = 0
    b = 0
    while a < len(x) and b < len(y):
        if x[a] < y[b]:
            new_list.append(x[a])
            a += 1
            continue
        elif y[b] < x[a]:
            new_list.append(y[b])
            b += 1
            continue
        else:
            new_list.append(x[a])
            a += 1
            continue

    for i in range (len(x)):   
        if x[i] not in new_list:
            new_list.append(x[i])
        
    print(new_list)


merge(list1,list2)
list1 = [3,1,2,7,]
list2 = [4,1,2,8,]

def my_union(x,y):
    union_list = []
    for i in range(len(x)):
        if x[i] not in union_list:
            union_list.append(x[i])
    for j in range(len(y)):
        if y[j] not in union_list:
            union_list.append(y[j])
    print(union_list)
    
def my_intersection(x,y):
    inter_list = []
    for i in range (len(x)):
        if x[i] in y:
            inter_list.append(x[i])
    print(inter_list)
    
def my_difference(x,y):
    diff_list = []
    for i in range (len(x)):
        if x[i] not in y:
            diff_list.append(x[i])
    print(diff_list)
            
    
my_union(list1,list2)
my_intersection(list1,list2)
my_difference(list1,list2)
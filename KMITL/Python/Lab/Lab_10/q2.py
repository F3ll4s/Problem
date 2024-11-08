list1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

def remove_the_thirds(x):
    for i in range(1,((len(x)+1)//3)+1):
        x.pop(i*2)

remove_the_thirds(list1)
print(list1)

remove_the_thirds(list1)
print(list1)

remove_the_thirds(list1)
print(list1)

def bubble_sort(x):
    list1 = x[:]
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
    print(list1)
bubble_sort([3,2,9,7,8])
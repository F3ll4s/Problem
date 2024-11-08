
def name_list():
    i = 0
    list = []
    while True:
        i += 1
        name = input(f"Enter name {i}:")
        list.append(name)
        if len(name) == 0:
            list.pop(len(list)-1)
            print(list)
            break
name_list()
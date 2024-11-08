def isAnagram(x,y):
    if len(x) == len(y):
        list = []
        for i in x:
            if i in y:
                list.append(i)
        if len(list) != len(x):
            return False
        else:
            return True
    else:
        return False
print(isAnagram("silent","listen"))
print(isAnagram("abyss","bystander"))

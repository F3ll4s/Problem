def inverse(x):
    same = dict()
    for key,val in x.items():
        if val not in same:
            same[val] = [key]
        else:
            same[val].append(key)
    return same
    

dex = {'a':'1','b':'2','c':'1','d':'3','e':'1','f':'2'}
print(inverse(dex))
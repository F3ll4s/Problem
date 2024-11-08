def find_duplicates(dict):
    result = {} 
    for i in dict:
        for j in dict:
            if i != j and dict[i] == dict[j]:
                result[i] = dict[i]
    return result

My = {'s5301':'Fred', 's5302':'Harry','s5303':'John','s5305':'Harry'}
print(find_duplicates(My))
def composite(dict1, dict2):
    result = {}
    for k, v in dict1.items():
        if v in dict2:
            result[k] = dict2[v]
    return result


dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd': 'p', 'e': 's'}
dict2 = {'p': '1', 'q': '2', 'r': '3', 's': '9'}
print(composite(dict1, dict2))

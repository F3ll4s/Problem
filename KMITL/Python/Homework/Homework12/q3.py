def product(*sets):
    if len(sets) == 1:
        return {(x,) for x in sets[0]}
    
    result = set()
    rest_product = product(*sets[1:])
    
    for x in sets[0]:
        for rest in rest_product:
            result.add((x,) + rest)
    
    return result

s1 = {1, 2, 3}
s2 = {'p', 'q'}
s3 = {'a', 'b', 'c'}

print(product(s1, s2))
print(product(s1, s2, s3))
print(product(s1))

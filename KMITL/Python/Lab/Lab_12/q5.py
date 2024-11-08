s = set([1,2,3])
def power(s):
    result = [frozenset([])]
    for i in s:
        result.append(frozenset([i]))
    
    for i in range(len(s)):
        for j in range (i,len(s)):
            result.append(frozenset([list(s)[i],list(s)[j]]))
            
    result.append(frozenset(s))
    
    return set(result)

print(power(s))
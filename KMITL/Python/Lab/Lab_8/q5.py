def LCS(s1,s2):
    longest = ""
    for x in range(len(s1)):
        for y in range(len(s2)):
            for z in range(len(s1)):
                for a in range(len(s2)):
                    if x < z + 1 and y < a+1 and s1[x:z+1] == s2[y:a+1] and len(s1[x:z+1]) > len(longest):
                        longest = s1[x:z+1]
    return longest    
    
                        # print(s1[x:z+1],s2[y:a+1])

print(LCS("War","Love"))

print(LCS("conition","fictional"))

print(LCS("smart","meter"))

print(LCS("back-end","front-end"))




        
    
        
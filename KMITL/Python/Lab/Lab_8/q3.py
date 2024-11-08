long_str = input("Long String:")
short_str = input("Short String: ")

position = []
result = []
answer = False
for i in range (len(long_str)):
    if short_str[0] == long_str[i]:
        position.append(i)
print(position)

for x in position:
    for y in range(len(short_str)):
        if x + y >= len(long_str):
            answer = False
            break
        elif long_str[x+y] == short_str[y]:
            answer = True
        else:
            answer = False
            
if answer == True:
    print("same")
else:
    print("Not same")
        
    
    
            







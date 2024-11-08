text = input("Enter some text: ")

check = []
count = 0
    
for x in range (len(text)):
    if text[x] in check:
        continue
    for y in range (len(text)):
         if text[x] == text[y]:
            count += 1
    percent = (count/len(text)) * 100
    print(f"{text[x]} {format(percent,".2f")}%")
    check.append(text[x]) 
    count = 0
    
    

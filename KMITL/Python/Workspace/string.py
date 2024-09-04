i = 1
x = 1
while i <= 9:
    while x <= 9 :
        if x != i:
            print(x,end="")
            x += 1
        else:
            x += 1
            continue
    print("")
    i += 1
    x = 1

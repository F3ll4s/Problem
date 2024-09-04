while True:
    x = int(input("Input: "))
    if x <= 0:
        print("Input Can't be Negative or Zero")
        continue
    elif x == 1:
        print("")
        break
    else:
        print("")
        for p in range(0,x):
            for i in range(0,x):
                print("*" * (i+1))
            for y in range(1,x-1):
                print("*" * (x-y))
            x -= 1
        break
print("*")
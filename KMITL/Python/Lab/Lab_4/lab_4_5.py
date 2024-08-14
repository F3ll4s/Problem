total = 0
lastnum = None
for i in range(5):
    x = int(input("Enter an integer: "))
    if lastnum != None and (lastnum < 0) != (x < 0):
        total = 0
    total += x
    lastnum = x
    print("Current SUm:     ",total)
        
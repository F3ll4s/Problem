import math

h = int(input("Enter the number of lines: "))
a = math.ceil(h/2)
b = math.floor(h/2)
for i in range (a):
    for x in range(i+1,0,-1):
        print(2**(x-1),end = "")
    print("")
for i in range (b):
    for z in range(b-i,0,-1):
        print(2**(z-1),end = "")
    print("")
    
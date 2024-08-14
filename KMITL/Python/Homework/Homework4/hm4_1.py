x1 = int(input("Enter Coordinate X in p1: "))
y1 = int(input("Enter Coordinate Y in p1: "))

x2 = int(input("Enter Coordinate X in p2: "))
y2 = int(input("Enter Coordinate Y in p2: "))

x3 = int(input("Enter Coordinate X in p3: "))
y3 = int(input("Enter Coordinate Y in p3: "))

if x2 == x1 :
    if x3 > x1:
        print("This is on the right side")
    elif x3 < x1 :
        print("This is on the left side")
    else:
        print("This is on the line ")
else:   
    slope = (y2 - y1)/(x2-x1)
    c = y1 - (slope * x1)
    if slope > 0:
        if y3 >= (slope*x3) + c:
            print("This point is on the left side")
        elif y3 <= (slope*x3) + c :
            print("This point is on the right side")
        else:
            print("This point is on the line ")
    elif slope < 0 :
        if y3 >= (slope*x3) + c:
            print("This point is on the right side")
        elif y3 <= (slope*x3) + c :
            print("This point is on the left side")
        else:
            print("This point is on the line ")
    elif slope == 0:
        if y3 <= c :
            print("This is below the line(Left side)")
        elif y3 >= c :
            print("This is above the line(Right side)")
        else:
            print("This is on the line")
    


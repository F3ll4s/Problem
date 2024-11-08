x1 = int(input("Enter Coordinate X in p0: "))
y1 = int(input("Enter Coordinate Y in p0: "))

x2 = int(input("Enter Coordinate X in p1: "))
y2 = int(input("Enter Coordinate Y in p1: "))

x3 = int(input("Enter Coordinate X in p2: "))
y3 = int(input("Enter Coordinate Y in p2: "))

if x2 == x1 :
    if x3 > x1:
        print("Point 2 is on the right side")
    elif x3 < x1 :
        print("Point 2 is on the left side")
    else:
        print("Point 2 is on the line ")
else:   
    slope = (y2 - y1)/(x2-x1)
    c = y1 - (slope * x1)
    if slope > 0:
        if y3 >= (slope*x3) + c:
            print("Point 2 is on the left side")
        elif y3 <= (slope*x3) + c :
            print("Point 2 is on the right side")
        else:
            print("Point 2 is on the line ")
    elif slope < 0 :
        if y3 >= (slope*x3) + c:
            print("Point 2 is on the right side")
        elif y3 <= (slope*x3) + c :
            print("Point 2 is on the left side")
        else:
            print("Point 2 is on the line ")
    elif slope == 0:
        if y3 <= c :
            print("Point 2 is below the line(Left side)")
        elif y3 >= c :
            print("Point 2 is above the line(Right side)")
        else:
            print("Point 2 is on the line")
    


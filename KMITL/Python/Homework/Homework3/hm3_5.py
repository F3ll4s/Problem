from turtle import *

x1 = int(input("Enter Coordinate X in p1: "))
y1 = int(input("Enter Coordinate Y in p1: "))

x2 = int(input("Enter Coordinate X in p2: "))
y2 = int(input("Enter Coordinate Y in p2: "))

x3 = int(input("Enter Coordinate X in p3: "))
y3 = int(input("Enter Coordinate Y in p3: "))
print(f"Point 1 :({x1},{y1})")
print(f"Point 2 : ({x2},{y2})")
print(f"Point 3 : ({x3},{y3})")

area = 0.5 * abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
penup()
goto(x1,y1)
pendown()
goto(x2,y2)
goto(x3,y3)
goto(x1,y1)
penup()
goto(min(x1,x2,x3),min(y1,y2,y3)-30)
pendown()
write(area)




exitonclick()
from turtle import *

x1 = int(input("Enter Coordinate X in p1: "))
y1 = int(input("Enter Coordinate Y in p1: "))
w1 = int(input("Enter the Width of the Rectangle 1: "))
h1 = int(input("Enter the Height of the Rectangle 1: "))

x2 = int(input("Enter Coordinate X in p2: "))
y2 = int(input("Enter Coordinate Y in p2: "))
w2 = int(input("Enter the Width of the Rectangle 2: "))
h2 = int(input("Enter the Height of the Rectangle 2: "))

left1 = x1-(w1/2)
right1 = x1+(w1/2)
left2 = x2-(w2/2)
right2 = x2+(w2/2)

up1 = y1+(h1/2)
down1 = y1-(h1/2)
up2 = y2+(h2/2)
down2 = y2-(h2/2)

l1 = (left1,up1)
r1 = (right1,down1)

l2 = (left2,up2)
r2 = (right2,down2)

penup()
goto(x1,y1)
pendown()
penup()
goto(left1,up1)
pendown()
goto(right1,up1)
goto(right1,down1)
goto(left1,down1)
goto(left1,up1)

penup()
goto(0,0)
goto(x2,y2)
pendown()
penup()
goto(left2,up2)
pendown()
goto(right2,up2)
goto(right2,down2)
goto(left2,down2)
goto(left2,up2)
penup()

print(l1)
print(r1)
print(l2)
print(r2)

if max(left1,left2) < min(right1,right2):
    if max(down1,down2) < min(up1,up2):
        print("Overlap")
else:
    print("Not Overlap")
if left1 <= left2 :
    if right2 <= right1:
        if up1 >= up2:
            if down2 >= down1:
                print("Rectangle 2 is inside Rectangle 1")
elif left2 <= left1:
    if right1 <= right2 :
        if up2 >= up1:
            if down1 >= down2:
                print("Rectangle 1 is inside Rectangle 2")
        
    
exitonclick()

from turtle import *
import turtle
import math

r = int(input("Enter Radius: "))
x = int(input("Enter Coordinate x: "))
y = int(input("Enter Coordinate y: "))
area = math.pi * r * r

penup()
goto(x,y)
pendown()
write(area)
penup()
goto(x,y-r)
pendown()
circle(r)
turtle.Screen().exitonclick()
//draw a circle and its radius display in the middle of the circle
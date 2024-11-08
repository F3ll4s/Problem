from turtle import *
n = int(input("Enter the row: "))

length = 100/n
for x in range(0,n):
    penup()
    goto(0,-length*x)
    pendown()
    for y in range (0,n):
        for i in range(4):
            forward(length)
            left(90)
        forward(length)


    



exitonclick()

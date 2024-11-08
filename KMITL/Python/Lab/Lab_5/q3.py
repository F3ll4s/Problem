from turtle import *
n = int(input("Enter the row: "))

length = 100/n
for x in range(0,n):
    penup()
    goto(0,length*x)
    pendown()
    if x % 2 == 1:
        for y in range (0,n):
            if  y % 2 == 0:
                fillcolor("black")
                begin_fill()
                for i in range(4):
                    forward(length)
                    left(90)
                end_fill()
            else:
                fillcolor("white")
                begin_fill()
                for i in range(4):
                    forward(length)
                    left(90)
                end_fill()
            forward(length)
    else:
        for y in range (0,n):
            if  y % 2 == 0:
                fillcolor("white")
                begin_fill()
                for i in range(4):
                    forward(length)
                    left(90)
                end_fill()
            else:
                fillcolor("black")
                begin_fill()
                for i in range(4):
                    forward(length)
                    left(90)
                end_fill()
            forward(length)


    



exitonclick()

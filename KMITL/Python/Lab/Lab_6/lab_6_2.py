from turtle import *
def draw_square(x):
        penup()
        goto(-x,x)
        pendown()
        goto(x,x)
        goto(x,-x)
        goto(-x,-x)
        goto(-x,x)
        
def big_square(x):
    for i in range(5):
        draw_square(x*i)
    forward(x*4)
    right(90)
    forward(x*8)
    left(90)
    forward(x*4)
    left(90)
    forward(x*4)
    left(90)
    forward(x*8)
    backward(x*4)
    right(180)

big_square(20)

exitonclick()
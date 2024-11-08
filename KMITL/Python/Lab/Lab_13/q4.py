from turtle import *

def cross(x,y):
    if y == 0:
        dot()
        return 
    for _ in range(4):
        forward(x)
        cross(x/2,y-1)
        backward(x)
        right(90)
        
cross(100,4)

exitonclick()
        

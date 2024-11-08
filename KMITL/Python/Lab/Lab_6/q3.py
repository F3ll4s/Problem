
from turtle import *

def draw_polygon(x,y,z=4,t=100):
    penup()
    goto(x,y)
    pendown()
    angle = 360/z
    
    forward(t)
    left(angle)
    forward(t)
    left(angle)
    forward(t)
    left(angle)      
    forward(t)
    left(angle)
    forward(t)
    left(angle)
    
        
draw_polygon(0,0)
draw_polygon(0,0,5)
draw_polygon(0,0,5,150)
        
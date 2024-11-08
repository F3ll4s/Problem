from turtle import *


length = int(input("Enter the length of the star: "))

penup()
goto(-100,0)
pendown()
forward(length)
right(144)
forward(length)
right(144)
forward(length)
right(144)
forward(length)
right(144)
forward(length)

exitonclick()
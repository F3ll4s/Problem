from turtle import *

text = input("Enter some text: ")
check = []
count = 0
countmax = 0
forward(40)
for x in range (len(text)):
    if text[x] in check:
        continue
    for y in range (len(text)):
        if text[x] == text[y]:
            count += 1
            if count > countmax:
                countmax = count
    check.append(text[x])
    penup()
    goto(xcor(),ycor()-20)
    write(text[x])
    goto(xcor(),ycor()+20)
    pendown()
    left(90)
    forward(20*count)
    right(90)
    forward(20)
    right(90)
    forward(20*count)
    left(90)
    forward(40)
    count = 0
goto(0,0)
left(90)
forward(countmax*20)
speed(0)
exitonclick()
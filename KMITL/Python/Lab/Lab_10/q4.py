import turtle as t

list1 = [1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4]

def draw(x):
    new_list = []
    for i in range(len(x)):
        if x[i] not in new_list:
            new_list.append(x[i])
    
    new_list.sort()
    for b in range(len(new_list)):
        count = 0
        countmax = 0
        for a in x:
            if x[b] == a:
                count += 1
                if count > countmax:
                    countmax = count
        t.penup()
        t.goto(t.xcor(),t.ycor()-20)
        t.write(new_list[b])
        t.goto(t.xcor(),t.ycor()+20)
        t.pendown()
        t.color("black")
        t.begin_fill()
        t.left(90)
        t.forward(20*count)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20*count)
        t.right(90)
        t.forward(20)
        t.end_fill()
        t.left(180)
        t.forward(20)
        
        
    t.goto(0,0)
    t.left(90)
    t.forward(countmax*20)
    t.exitonclick()
t.speed(100)            
draw(list1)

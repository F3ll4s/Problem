from turtle import *
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = [" Su","  Mo","  Tu","  We","  Th","  Fr","  Sa"]

speed(100)
b = -700
c = 350
d = 0
cday = 1
skip = 1


for f in range(1,4):
    c -=  d + 50
    sike = (f"Month # {f}")
    print(sike)
    if f == 3:
        mok = 8
    else:
        mok = 7
    for x in range(0,mok):
        penup()
        goto(b,c+(-25*x))
        pendown()
        d = 25*x
        for y in range (0,7):
            if x == 0:
                write(sike)
                for z in range(2):
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                break
            elif x == 1:
                write("  ")
                write(day[y])
                for i in range(4):
                    forward(25)
                    left(90)
            elif  x >= 2:
                for i in range(4):
                    forward(25)
                    left(90)
                if skip > 0 :
                    write(" ")
                    skip -=1
                elif cday <= days_in_month[f-1]:
                    penup()
                    forward(5)
                    write(cday)
                    back(5)
                    pendown()
                    cday += 1
                    if cday > days_in_month[f-1]:
                        cday = 1
                        skip = 7
            
            forward(25)           
    continue

c = 350
d = 0
for f in range(4,7):
    c -=  d + 50
    sike = (f"Month # {f}")
    print(sike)
    if f == 6:
        mok = 8
    else:
        mok = 7
    for x in range(0,mok):
        penup()
        goto(b+200,c+(-25*x))
        pendown()
        d = 25*x
        for y in range (0,7):
            if x == 0:
                write(sike)
                for z in range(2):
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                break
            elif x == 1:
                write("  ")
                write(day[y])
                for i in range(4):
                    forward(25)
                    left(90)
            elif  x >= 2:
                for i in range(4):
                    forward(25)
                    left(90)
                    
                if skip > 0 :
                    write(" ")
                    skip -=1
                elif cday <= days_in_month[f-1]:
                    penup()
                    forward(5)
                    write(cday)
                    back(5)
                    pendown()
                    cday += 1
                    if cday > days_in_month[f-1]:
                        cday = 1
                        skip = 7
            
            forward(25)           
    continue

c = 350
d = 0
for f in range(7,10):
    c -=  d + 50
    sike = (f"Month # {f}")
    print(sike)
    if f == 9:
        skip = 0
    for x in range(0,7):
        penup()
        goto(b+400,c+(-25*x))
        pendown()
        d = 25*x
        for y in range (0,7):
            if x == 0:
                write(sike)
                for z in range(2):
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                break
            elif x == 1:
                write("  ")
                write(day[y])
                for i in range(4):
                    forward(25)
                    left(90)
            elif  x >= 2:
                for i in range(4):
                    forward(25)
                    left(90)
                    
                if skip > 0 :
                    write(" ")
                    skip -=1
                elif cday <= days_in_month[f-1]:
                    penup()
                    forward(5)
                    write(cday)
                    back(5)
                    pendown()
                    cday += 1
                    if cday > days_in_month[f-1]:
                        cday = 1
                        skip = 7
            
            forward(25)           
    continue

c = 350
d = 0
for f in range(10,13):
    c -=  d + 50
    sike = (f"Month # {f}")
    print(sike)
    if f == 12:
        skip = 0
    for x in range(0,7):
        penup()
        goto(b+600,c+(-25*x))
        pendown()
        d = 25*x
        for y in range (0,7):
            if x == 0:
                write(sike)
                for z in range(2):
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                break
            elif x == 1:
                write("  ")
                write(day[y])
                for i in range(4):
                    forward(25)
                    left(90)
            elif  x >= 2:
                for i in range(4):
                    forward(25)
                    left(90)
                    
                if skip > 0 :
                    write(" ")
                    skip -=1
                elif cday <= days_in_month[f-1]:
                    penup()
                    forward(5)
                    write(cday)
                    back(5)
                    pendown()
                    cday += 1
                    if cday > days_in_month[f-1]:
                        cday = 1
                        skip = 7
            
            forward(25)           
    continue
               
exitonclick()
from turtle import *

day = [" Su","  Mo","  Tu","  We","  Th","  Fr","  Sa"]
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

speed(1000)
b = -700
c = 350
d = 0
f = 1
skip = 1

while f <= 3:
    c -= d + 50
    sike = f"Month # {f}"
    print(sike)
    current_day = 1
    x = 0
    while x < 7:
        penup()
        goto(b, c + (-25 * x))
        pendown()
        d = 25 * x
        y = 0
        while y < 7:
            if x == 0:
                write(sike)
                z = 0
                while z < 2:
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                    z += 1
                break
            elif x == 1:
                write("  ")
                write(day[y])
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            elif x >= 2:
                
                if skip > 0 :
                    write(" ")
        
                elif current_day <= days_in_month[f-1]:
                    write(f" {current_day:2d}")
                    current_day += 1
                elif current_day == days_in_month[f-1] + 1:
                    skip += 7
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
                skip -= 1
            forward(25)
            y += 1
        x += 1
    f += 1

c = 350
d = 0
f = 4

while f <= 6:
    c -= d + 50
    sike = f"Month # {f}"
    print(sike)
    current_day = 1
    x = 0
    while x < 7:
        penup()
        goto(b + 200, c + (-25 * x))
        pendown()
        d = 25 * x
        y = 0
        while y < 7:
            if x == 0:
                write(sike)
                z = 0
                while z < 2:
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                    z += 1
                break
            elif x == 1:
                write("  ")
                write(day[y])
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            elif x >= 2:
                if current_day <= days_in_month[f-1]:
                    write(f" {current_day:2d}")
                    current_day += 1
                else:
                    write("   ")
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            forward(25)
            y += 1
        x += 1
    f += 1

c = 350
d = 0
f = 7

while f <= 9:
    c -= d + 50
    sike = f"Month # {f}"
    print(sike)
    current_day = 1
    x = 0
    while x < 7:
        penup()
        goto(b + 400, c + (-25 * x))
        pendown()
        d = 25 * x
        y = 0
        while y < 7:
            if x == 0:
                write(sike)
                z = 0
                while z < 2:
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                    z += 1
                break
            elif x == 1:
                write("  ")
                write(day[y])
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            elif x >= 2:
                if current_day <= days_in_month[f-1]:
                    write(f" {current_day:2d}")
                    current_day += 1
                else:
                    write("   ")
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            forward(25)
            y += 1
        x += 1
    f += 1

c = 350
d = 0
f = 10

while f <= 12:
    c -= d + 50
    sike = f"Month # {f}"
    print(sike)
    current_day = 1
    x = 0
    while x < 7:
        penup()
        goto(b + 600, c + (-25 * x))
        pendown()
        d = 25 * x
        y = 0
        while y < 7:
            if x == 0:
                write(sike)
                z = 0
                while z < 2:
                    forward(175)
                    left(90)
                    forward(25)
                    left(90)
                    z += 1
                break
            elif x == 1:
                write("  ")
                write(day[y])
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            elif x >= 2:
                if current_day <= days_in_month[f-1]:
                    write(f" {current_day:2d}")
                    current_day += 1
                else:
                    write("   ")
                i = 0
                while i < 4:
                    forward(25)
                    left(90)
                    i += 1
            forward(25)
            y += 1
        x += 1
    f += 1

exitonclick()

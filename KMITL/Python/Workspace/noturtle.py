from turtle import *
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["  Mo","  Tu","  We","  Th","  Fr","  Sa"," Su"]

speed(100)
b = -700
c = 350
d = 0
cday = 1
skip = 1

f = int(input("Enter Month: "))
c -=  d + 50
sike = (f"Month # {f}")
print(sike)
if f == 3 or f == 6:
    mok = 8
elif f == 9 or f == 12:
    skip = 0
else:
    mok = 7
for x in range(0,mok):
    penup()
    goto(0,-x*25)
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


exitonclick()
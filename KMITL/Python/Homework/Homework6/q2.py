from turtle import *
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["  Mo","  Tu","  We","  Th","  Fr","  Sa"," Su"]
month = ["January 2024", "February 2024", "March 2024", "April 2024", "May 2024", "June 2024", "July 2024", "August 2024", "September 2024", "October 2024", "November 2024", "December 2024"]
speed(100)
b = -700

def get_month(f):
    c = 350
    d = 0
    cday = 1
    skip = 1
    c -=  d + 50
    sike = month[f-1]
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
get_month(2)

exitonclick()
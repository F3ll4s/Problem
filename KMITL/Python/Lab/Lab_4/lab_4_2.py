
x = eval(input("Enter the number: "))

if type(x) == int:
    z = int(input("Display in binary(0), octal(1), hexadecimal(2): "))
    if z == 0:
        print(format(x),"b")
    elif z == 1:
        print(oct(x))
    elif z == 2:
        print(hex(x))
    else:
        print("Wrong Input")
elif type(x) == float:
    y = int(input("Display in float(0),scientific format(1): "))
    if y == 0:
        print(format(x,".2f"))
    elif y == 1:
        print(format(x,"e"))
else:
    print("I dont know")
    
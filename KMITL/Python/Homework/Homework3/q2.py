digits = int(input("Enter a four-digit integer: "));

d_1 = digits // 1000
dd_2 = digits // 100
dd_3 = digits // 10
d_2 = dd_2 % 10
d_3 = dd_3 % 10
d_4 = digits % 10



print(d_4 , end = "")
print(d_3 , end = "")
print(d_2 , end = "")
print(d_1 , end = "")
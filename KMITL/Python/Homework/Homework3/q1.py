import math

a = str(input("Enter employee's name: "))
b = float(input("Enter number of hours worked in a week: "))
c = float(input("Enter hourly pay rate: "))
d = float(input("Enter federal tax withholdding rate: "))
e = float(input("Enter state tax withholding rate: "))

g = format(b,".1f")
f = format(c,".2f")
grosspay = b * c
fed = d * 100
fedtax = grosspay * d
sta = e * 100
statax = grosspay * e
total = fedtax + statax
fstatax = format(math.floor(statax,".2f"))
ftotal = format(total,".2f")
fltotal = float(ftotal)
realtotal = grosspay - fltotal

print("")
print("Employee's name: ",a)
print("Hour Worked:",g)
print("Pay Rate: $", f)
print("Gross Pay: $",grosspay)
print("Deductions:")
print("  Federal Withholding ({})% : $".format(fed), fedtax)
print("  State Withholding ({})% : $".format(sta), fstatax)
print("  Total Deduction: $", ftotal)
print("Net pay: $", realtotal)

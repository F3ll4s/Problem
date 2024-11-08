money = int(input("Input your amount of money: "))
thousand = money // 1000
fivehundred = (money % 1000)//500
hundred = ((money % 1000) % 500)//100
fifty = (money % 100) // 50
twenty = ((money % 100) % 50) // 20
tenth = (((money % 100) % 50) % 20) // 10
five = (money % 10) // 5
two = ((money % 10) % 5) // 2
oneth = ((money % 10) % 5) % 2

if thousand != 0:
    print(f"1000-Baht notes: {thousand}")
if fivehundred != 0:
    print(f"500-Baht notes: {fivehundred}")
if hundred != 0:
    print(f"100-Baht notes: {hundred}")
if fifty != 0:
    print(f"50-Baht notes: {fifty}")
if twenty != 0:
    print(f"20-Baht notes: {twenty}")
if tenth != 0:
    print(f"10-Baht notes: {tenth}")
if five != 0:
    print(f"5-Baht notes: {five}")
if two != 0:
    print(f"2-Baht notes: {two}")
if oneth != 0:
    print(f"1-Baht notes: {oneth}")

binary = int(input("Enter number: "))

idk =""
while binary > 0:
    num1 = binary % 2
    idk = str(num1) + idk
    binary //= 2

print(f"Binary is of this number is {idk}")
total = 0

for i in range (len(idk)):
    total += (2**(len(idk)-(i+1))) * int(idk[i])
print(f"Number of Binary is {total}")
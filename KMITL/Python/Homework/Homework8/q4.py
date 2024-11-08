result = 0
isbn = ""
while True:
    isbn = input("Enter the first 9 digits of an ISBN-10 as a string: ")
    if isbn.isdigit() and len(isbn) == 9:
        break
    else:
        print("Try again")

for i in range (len(isbn)):
    result += int(isbn[i]) * (i+1)
remainder = result % 11

if remainder == 10:
    print("Your ISBN-10 Number is ",end="")
    for x in range (9):
        print(int(isbn[x]),end="")
    print("X")
else:
    print("Your ISBN-10 Number is ",end="")
    for y in range (9):
        print(int(isbn[y]),end="")
    print(remainder)

        
    
        


        
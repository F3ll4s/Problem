oneth = ["zero","one","two","three","four","five","six","seven","eight","nine"]
tenty = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
eleven =["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
i = 0
number = str(input("Enter a number: "))

for x in number:
    i += 1
    
no = int(number)
if i == 1:
    print(oneth[no])
if i == 2:
    ten = no // 10
    one = no % 10
    if ten == 1:
        print(eleven[one])
    
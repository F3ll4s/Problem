oneth = ["zero","one","two","three","four","five","six","seven","eight","nine"]
tenty = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
eleven =["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
while True:
    number = int(input("Enter a number: "))
    ten = number // 10
    hundred = number // 100
    if number < 1000:
        if number < 10:
            print(oneth[number])
        if 11 <= number <= 19:
            print(eleven[(number % 10)-1])
        if  0 < ten < 10 :
            one = number % 10
            if one > 0:
                print(f"{tenty[ten-1]}-{oneth[one]}")
            else:
                print(tenty[ten-1])
        if 0 < hundred < 10:
            tenth = ten % 10
            one = number % 10
            if tenth > 0 and one == 0:
                print(f"{oneth[hundred]} hundred and {tenty[tenth-1]}")
            if tenth > 0 and one > 0:
                print(f"{oneth[hundred]} hundred and {tenty[tenth-1]}-{oneth[one]}")
            if tenth == 0 and one == 0:
                print(f"{oneth[hundred]} hundred")
            if tenth == 0 and one > 0:
                print(f"{oneth[hundred]} hundred and {oneth[one]}")
        else:
            if hundred == 0:
                continue;
            else:
                print(oneth[hundred] + " hundred")
    else:
        print("I dont know")

        
                
                
    
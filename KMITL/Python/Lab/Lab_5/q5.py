

while True :
    x = input("Enter a character: ")
    if 48 <= ord(x) <= 57:
        print(f">>{x} is a numeric character")
        continue
    elif 97 <= ord(x) <= 122:
        print(f">>{x} is a small-case letter and its capital letter is {x.upper()}",)
        continue
    elif 65 <= ord(x) <= 90:
        print(f">>{x} is a capital letter and its small-case letter is {x.lower()}")
        continue
    elif ord(x) == 9:
        print(f'Goodbye, see you tmr')
        break
    else: 
        print(f">>{x} is a special character.")
        continue


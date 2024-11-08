while True:
    n = input("Enter number that is > 0: ")
    if n.isdigit():
        n= int(n)
        if n > 0:
            break
    print("try agian")
guess = n/2
sqrt = n**0.5
for i in range (0,8):
    temp = float(n/guess)
    guess = (guess + temp)/2
    while i >= 5:
        print(f"Iteration {i} :", format(guess,".3f"))
        break
print(f"The square root of {n} is ", format(sqrt,".3f"))
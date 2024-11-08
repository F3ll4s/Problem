import random

x = int(input("scissor(0), rock(1), paper(2): "))

y = random.randint(0,2)

if x == 0:
    if y == 0:
        print("The computer is scissor. You are scissor. It is a draw")
    elif y == 1:
        print("The computer is rock. You are scissor. You Lose")
    else:
        print("The computer is paper. You are scissor. You Win")
elif x == 1:
    if y == 0:
        print("The computer is scissor. You are rock. You Win")
    elif y == 1:
        print("The computer is rock. You are rock. It is a draw")
    else:
        print("The computer is paper. You are rock. You Lose")
elif x == 2:
    if y == 0:
        print("The computer is scissor. You are paper. You Lose")
    elif y == 1:
        print("The computer is rock. You are paper. You Win")
    else:
        print("The computer is paper. You are paper. It is a draw")
else:
    print("Wrong Input")
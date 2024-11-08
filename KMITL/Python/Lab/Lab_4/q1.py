x = int(input("Enter the score"))

if 80 <= x <= 100 :
    print("Grade A")
elif 70 <= x < 80 :
    print("Grade B")
elif 60 <= x < 70 :
    print("Grade C")
elif 50 <= x < 60 :
    print("Grade D")
elif 0 <= x < 50:
    print("Grade F")
else:
    print("Score In range 0 - 100")
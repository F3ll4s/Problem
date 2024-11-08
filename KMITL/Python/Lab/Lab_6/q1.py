def score(x):
    grade = ""
    if 80 <= x <= 100 :
        grade = "A"
    elif 70 <= x < 80 :
        grade = "B"
    elif 60 <= x < 70 :
        grade = "C"
    elif 50 <= x < 60 :
        grade = "D"
    elif 0 <= x < 50:
        grade = "F"
    else:
        grade = "Invalid score"
    return grade

print(score(80))
print(score(101))
print(score(-2))
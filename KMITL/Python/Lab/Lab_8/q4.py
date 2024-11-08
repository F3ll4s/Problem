first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
while True:
    gender = input("Enter your gender(m/f): ")
    if gender == 'm' or gender == 'f':
        upper_first = first_name.upper()
        upper_last = last_name[0].upper()
        upper_gender = gender.upper()
        print(f"Your username: {upper_gender}{upper_last}{upper_first}")
        break;
    else:
        continue;
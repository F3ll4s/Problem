import random

# Organs and their fictional prices
organs = {
    "Kidney": 50000,
    "Liver": 75000,
    "Lung": 75000,
    "Eye": 5000,
    "Bone Marrow": 25000
}

sold_organs = []  # List to keep track of sold organs
choice = 0
money = int(input("How much money did you bring: "))
begin = money

while choice != "stop":
    if money == 0:
        print("You ran out of money.")
        sell_choice = input("Do you need more money? Type 'yes' to sell an organ, 'no' to stop playing: ").lower()

        if sell_choice == "yes":
            print("Choose an organ to sell:")
            for index, organ in enumerate(organs, 1):
                print(f"({index}) {organ}: ${organs[organ]}")
            print("(9) Cancel")
            
            organ_choice = int(input())
            
            if organ_choice in range(1, len(organs) + 1):
                selected_organ = list(organs.keys())[organ_choice - 1]
                money += organs[selected_organ]
                sold_organs.append(selected_organ)  # Track the sold organ
                print(f"You sold your {selected_organ} for ${organs[selected_organ]}.")
                print(f"Your new balance is: ${money}")
            else:
                print("Cancelled.")
        else:
            print("You stopped playing.")
            break

    print("(1) Purple x2 , (2) Green x14 , (3) Black x2 , (4) Spacial x7 , (9) Exit")
    choose = int(input())
    
    match choose:
        case 1:
            choice = "Purple"
        case 2:
            choice = "Green"
        case 3:
            choice = "Black"
        case 4:
            choice = "Spacial"
        case 9:
            break
        case _:
            choice = "None"
    
    if choice == "None":
        print("Invalid Input")
    else:
        check = False
        while not check:
            bet = int(input("How much you wanna bet for: "))
            if money >= bet:
                money -= bet
                check = True
            else:
                print("You are broke. Don't make yourself in debt, please.")

        result2 = ""

        rng = random.randrange(1, 17)
        if rng == 9:
            result = "Green"
            times = 14
        elif rng == 16:
            result = "Spacial"
            result2 = "Purple"
            times = 7
            extra = 2
        elif rng == 10:
            result = "Spacial"
            result2 = "Black"
            times = 7
            extra = 2
        elif rng % 2 == 0:
            result = "Black"
            times = 2
        else:
            result = "Purple"
            times = 2
        
        print("It rolls", result, result2)
        
        if choice == result:
            gain = bet * times
            money += gain
        elif choice == result2:
            gain = bet * extra
            money += gain
        else:
            gain = 0
        
        if gain == 0:
            print("You lose the bet this time.")
        else:
            print("You Won! You gain:", gain)
        
        print()
        print("Your balance is now:", money)
    
# Calculate profit or loss
if money > begin:
    print("You Have Made", money - begin, "$ Profit!!!")
elif money == begin:
    print("You didn't gain or lose any money.")
else:
    print("You lost", begin - money, "$.")

# Print a summary of organs sold
if sold_organs:
    print("\nOrgans that you lost:")
    for organ in sold_organs:
        print(f"- {organ}")
else:
    print("\nYou didn't sell any organs.")
  
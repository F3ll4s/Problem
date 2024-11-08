contact = {}
while True:
    print("Phonebook Manager")
    print('Press "+" to add a new contact')
    print('Press "-" to delete a contact')
    print('Press "f" to find a contact')
    print('Press "p" to print out all contacts in the phonebook')
    choice = input('Press "q" to quit the program \n')
    match choice:
        case "+" :
            name = input("Enter name:")
            contact[name] = input("Enter Phone Number: ")
        case "-":
            del_name = input("Type Name to delete contact: ")
            if del_name in contact.keys():
                del contact[del_name]
            else:
                print(f"{del_name} not in ur contact")
        case "f":
            find = input("Find a contact:")
            if find in contact.keys():
                print(f"{find} is in your contact")
            else:
                print(f"{find} is not in your contact")
        case "p":
            print(contact)
        case "q":
            print("Goodbye")
            break
        case _:
            print("Try again")
            continue
        
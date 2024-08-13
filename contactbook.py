contact = {}
while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact\n 4. Edit contact \n 5. Delete contact\n 6. Exit\n Enter your choice "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print( "contact number is ", contact[search_name],search_name)
        else:
            print("Name not found in the contact book")
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            print("Name\tContact Number")
            for key in contact:
                print("{}\t{}".format(key, contact[key]))
    elif choice == 4:
        edit_contact = input("Enter the number to be edited: ")
        if edit_contact in contact:
            phone = input("Enter the new mobile number: ")
            contact[edit_contact] = phone
            print("Contact updated")
            print("Name\tContact Number")
            for key in contact:
                print("{}\t{}".format(key, contact[key]))
        else:
            print("Name not found in the contact book")
    elif choice == 5:
        delete_contact = input("Enter the contact to be deleted: ")
        if delete_contact in contact:
            confirm = input("Do you want to delete this contact? (y/n) ")
            if confirm.lower() == 'y':
                del contact[delete_contact]
                print("Contact deleted successfully")
                print("Name\tContact Number")
                for key in contact:
                    print("{}\t{}".format(key, contact[key]))
            else:
                print("Contact deletion canceled")
        else:
            print("Name is not found in the contact book")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

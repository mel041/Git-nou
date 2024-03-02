def main():
    # Displaying the welcome message
    print("Welcome to the phone book!!")

    agenda = {}# Creating an empty dictionary to store contacts

    while True: # Infinite loop to show menu and receive options from user

        print("1. Add contact") # Option to add a new contact
        print("2. View contacts")
        print("3. Search contact")
        print("4. Exit")
        
        opcion = input("Select an option (1/2/3/4): ")
        
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            ver_contactos(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            print("¡See you soon!")
            break
        else:
            print("Invalid option. Please select a valid option.")
def main():
    # Displaying the welcome message
    print("Welcome to the phone book!!")

    agenda = {}# Creating an empty dictionary to store contacts

    while True: # Infinite loop to show menu and receive options from user

        print("1. Add contact") # Option to add a new contact
        print("2. View contacts") # Option to view contact list
        print("3. Search contact") # Option to search for a contact
        print("4. Exit") # Option to exit the program
        
        opcion = input("Select an option (1/2/3/4): ") # We ask the user to select an option
        
        if opcion == "1":   # If the user chooses option 1 
                            #we call the agregar_contactos function to add a new contact
            agregar_contacto(agenda)

        elif opcion == "2": # If the user chooses option 2
                            # We call the ver_contactos function to display the contact list
            ver_contactos(agenda)
        elif opcion == "3": # If the user chooses option 3
                            # We call the buscar_contacto function to search for a contact
            buscar_contacto(agenda)
        elif opcion == "4": # If the user chooses option 4
            print("¡See you soon!") # Goodbye message
            break   # We exit the loop, ending the program
        else:   #If the user enters an invalid option
            print("Invalid option. Please select a valid option.") # Invalid option message
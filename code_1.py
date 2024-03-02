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
            
def agregar_contacto(agenda):
    # Ask the user to input the contact's name
    nombre = input("Enter the contact's name: ")
    # Ask the user to input the contact's phone number
    telefono = input("Enter the contact's phone number: ")
    # Add the contact to the phonebook
    agenda[nombre] = telefono
    # Print a success message
    print("Contact added successfully.")

def ver_contactos(agenda):
    # Check if the phonebook is empty
    if len(agenda) == 0:
        print("The phonebook is empty.")
    else:
        # Print the list of contacts
        print("Contact list:")
        # Loop through the items in the phonebook and print each contact's name and phone number
        for nombre, telefono in agenda.items():
              # For each tuple pair, print the contact's name and phone number. 
              # 'nombre' is the variable representing the contact's name and 'telefono' is the variable representing the contact's phone number.
            print("Name:", nombre, "\tPhone number:", telefono)

def buscar_contacto(agenda):
    # Ask the user to input the name of the contact they want to search for
    nombre = input("Enter the name of the contact you want to search for: ")
    # Check if the contact is in the phonebook
    if nombre in agenda:
        # Print the contact's name and phone number
        print("Name:", nombre, "\tPhone number:", agenda[nombre])
    else:
        # Print a message saying the contact is not in the phonebook
        print("The contact is not in the phonebook.")

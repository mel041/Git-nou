def main():
    print("Welcome to the phone book!!")
    agenda = {}

    while True:
        print("1. Add contact")
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
            print("¡S!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
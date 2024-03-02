def agregar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono del contacto: ")
    agenda[nombre] = telefono
    print("Contacto agregado exitosamente.")

def ver_contactos(agenda):
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print("Nombre:", nombre, "\tTeléfono:", telefono)

def buscar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    if nombre in agenda:
        print("Nombre:", nombre, "\tTeléfono:", agenda[nombre])
    else:
        print("El contacto no se encuentra en la agenda.")
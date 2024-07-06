
informacion_cliente = []
def registro_pedido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingresa su apellido: ")
    contacto = input("Ingresa su contacto telefónico: ")
    evento = input("Ingrese tipo de evento: ")
    Menu_comida = input("Ingrese el número de menú de comida deseado:\n1) Comida Italiana\n2) Comida Japonesa\n3) BBQ\nSeleccione la opción: ")

    cliente = {
        "Nombre del cliente": nombre,
        "Apellido del cliente": apellido,
        "Contacto": contacto,
        "Evento": evento,
        "Menu": Menu_comida
    }
    informacion_cliente.append(cliente)
    print("\n*Su pedido ha sido registrado*")

def detalle_pedido(cliente):
    print("\nDetalle del pedido solicitado.")
    for i, cliente in enumerate(informacion_cliente, start=1):
        print(f"{i}. {cliente['nombre']} {cliente['apellido']} {cliente['Contacto']} {cliente['Menu']} {cliente['Menu']}")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar pedido")
        print("2. Imprimir detalle del pedido")
        print("3. ----Imprimir detalle")
        print("4. Salir del programa")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registro_pedido()
        elif opcion == "2":
            detalle_pedido()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

print(menu())
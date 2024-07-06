import json

informacion_cliente = []

def registro_pedido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingresa su apellido: ")
    contacto = input("Ingresa su contacto telefónico: ")
    evento = input("Ingrese tipo de evento: ")
    Menu_comida = input("Ingrese el número de menú de comida deseado:\nComida Italiana\nComida Japonesa\nBBQ\nEscriba la opción: ")

    cliente = {
        "Nombre del cliente": nombre,
        "Apellido del cliente": apellido,
        "Contacto": contacto,
        "Evento": evento,
        "Menu": Menu_comida
    }
    informacion_cliente.append(cliente)
    print("\n*Su pedido ha sido registrado*")

def detalle_pedido():
    print("\nDetalle del pedido solicitado.")
    for i, cliente in enumerate(informacion_cliente, start=1):
        print(f"{i}. {cliente['Nombre del cliente']} {cliente['Apellido del cliente']} {cliente['Contacto']} {cliente['Evento']} ({cliente['Menu']})")

def crear_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")

def crear_texto(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"{i}. {contenido['Nombre del cliente']} {contenido['Apellido del cliente']} {contenido['Contacto']} {contenido['Evento']} ({contenido['Menu']})")
    print(f"archivo: {nombre_archivo} creado exitosamente")


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
        elif opcion == "3":
            crear_json('Registro.json', informacion_cliente)
            crear_texto('Registro', detalle_pedido)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

print(menu())
#Proyecto VK
estoque = {}

#Mostrar menu de opciones
def mostrar_menu():
    print("Bienvenido al gestor de invetario de VK")
    print("[1] Agregar producto")
    print("[2] Actualizar producto")
    print("[3] Eliminar producto")
    print("[4] Mostrar todos los productos")
    print("[0] Salir")

#Agregar productos XDD
def Agregar_producto(stock):
    Nombre = input("Ponga el nombre del producto").strip().lower()

    #Verificar si el producto existe en el inventario
    if Nombre == "":
        print("Nombre invalido. Por favor, ingrese un nombre válido.")
        return

    try:
        precio = float(input("Precio del producto: "))
        Cantidad = int(input("Cantidad del producto: "))
    except ValueError:
        print("Valor invalido. Por favor, ingrese un precio y cantidad válidos. ")
        return

    #Sí ya existe el producto, sumar cantidades
    if Nombre in stock:
        stock[Nombre]["Cantidad"] += Cantidad
        print(f"Se ha actualizado correctamente el producto {stock[Nombre]['Nombre'][Cantidad]}")
    else:
        #Crear producto nuevo
        stock[Nombre] = {
            "Precio": precio,
            "Cantidad": Cantidad
        }
        print(f"producto {Nombre} Registrado correctamente.")

#Actualizar producto
def Actualizar_producto(stock):
    Nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()

    #Verificar sí existe el producto
    if Nombre not in stock:
        print(f"producto {Nombre} No existe en el inventario.")
        return

    print("[1] Actualizar precio")
    print("[2] Actualizar cantidad")
    opción = input("Selecciona una opción")

    try:
        if opción == "1":
            Nuevo_precio = float(input("Ingrese el nuevo precio bro: "))
            stock[Nombre]["Precio"] = Nuevo_precio
            print(f"Precio del producto {Nombre} Actualizado correctamente.")
        elif opción == "2":
            Nueva_cantidad = int(input("Ingrese la nueva cantidad:"))
            stock[Nombre]["Cantidad"] = Nueva_cantidad
            print(f"Cantidad del producto {Nombre} Actualizado correctamente. ")
        else:
            print("Opción invalida. Por favor, seleccione una opción válida.")
    except ValueError:
        print("Valor invalido. Por favor, ingrese un precio o cantidad válidos. ")

#Remover productos
def Eliminar_producto(stock):
    Nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()

    if Nombre in stock:
        del stock[Nombre]
        print(f"Producto {Nombre} eliminado. ")
    else:
        print(f"Producto{Nombre} no existe mae. ")

#Mira el inventario
def Mostrar_inventario(stock):
    print("\n[1]------ Inventario ---")
    print("[2] Buscar productos por nombre")
    print("[3] Volver al menu principal")

    Opción = input("Opción: ")

    #Mostrar todos los productos
    if Opción == "1":
        if not stock:
            print("Inventario vacio. ")
            return

        print("\n--- Inventario ---")
        for Nombre, datos in stock.items():
            print(f"Producto: {Nombre}")
            print(f"Precio: R${datos['Precio']}")
            print(f"Cantidad: {datos['Cantidad']}")
            print("--------------------")

    #Buscar productos por nombre
    elif Opción == "2":
        Nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        if Nombre in stock:
            print(f"\n--- Producto ---")
            print(f"Producto: {Nombre}")
            print(f"Precio: R${stock[Nombre]['Precio']}")
            print(f"Cantidad: {stock[Nombre]['Cantidad']}")
        else:
            print(f"Producto {Nombre} no encontrado en el inventario. ")

    elif Opción == "3":
        return
    else:
        print("Opción invalida cochon. Por favor, seleccione una opición valida.")

#Mierda principal
while True:
    mostrar_menu()
    opción = input("Seleccione una opción: ")

    if opción == "1":
        Agregar_producto(estoque)
    elif opción == "2":
        Actualizar_producto(estoque)
    elif opción == "3":
        Eliminar_producto(estoque)
    elif opción == "4":
        Mostrar_inventario(estoque)
    elif opción == "0":
        print("Saliendo del programa. ")
        break
    else:
        print("Opción invalida. ")
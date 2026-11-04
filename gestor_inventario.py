    #Gestor de inventario para el proyecto VK
"""Gestor de inventario para el proyecto VK"""
#Mostrar menu de opciones
def mostrar_menu():
    """Mostrar el menú de opciones del gestor de inventario"""
    print("Bienvenido al gestor de inventario de VK")
    print("[1] Agregar producto")
    print("[2] Actualizar producto")
    print("[3] Eliminar producto")
    print("[4] Mostrar todos los productos")
    print("[0] Salir")

#Agregar productos
def agregar_producto(stock):
    """Agregar un producto al inventario"""
    nombre = input("Ponga el nombre del producto: ").strip().lower()

    #Verificar si el producto existe en el inventario
    if nombre == "":
        print("Nombre invalido. Por favor, ingrese un nombre válido.")
        return

    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
    except ValueError:
        print("Valor invalido. Por favor, ingrese un precio y cantidad válidos. ")
        return
    if precio < 0 or cantidad < 0:
        print("El precio y la cantidad no pueden ser negativos.")
        return

    #Sí ya existe el producto, sumar cantidades
    if nombre in stock:
        stock[nombre]["Cantidad"] += cantidad
        stock[nombre]["Precio"] = precio
        print(f"Se ha actualizado {nombre}. Cantidad total: {stock[nombre]['Cantidad']}")
    else:
        #Crear producto nuevo
        stock[nombre] = {
            "Precio": precio,
            "Cantidad": cantidad
        }
        print(f"producto {nombre} Registrado correctamente.")

#Actualizar producto
def actualizar_producto(stock):
    """Actualizar un producto existente en el inventario"""
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()

    #Verificar que el producto exista
    if nombre not in stock:
        print(f"producto {nombre} No existe en el inventario.")
        return

    print("[1] Actualizar precio")
    print("[2] Actualizar cantidad")
    opcion = input("Selecciona una opción: ")

    try:
        if opcion == "1":
            nuevo_precio = float(input("Ingrese el nuevo precio bro: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.")
                return
            stock[nombre]["Precio"] = nuevo_precio
            print(f"Precio del producto {nombre} Actualizado correctamente.")
        elif opcion == "2":
            nueva_cantidad = int(input("Ingrese la nueva cantidad:"))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
            stock[nombre]["Cantidad"] = nueva_cantidad
            print(f"Cantidad del producto {nombre} Actualizado correctamente. ")
        else:
            print("Opción invalida. Por favor, seleccione una opción válida.")
    except ValueError:
        print("Valor invalido. Por favor, ingrese un precio o cantidad válidos. ")

#Remover productos
def eliminar_producto(stock):
    """Eliminar un producto del inventario"""
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()

    if nombre in stock:
        del stock[nombre]
        print(f"Producto {nombre} eliminado. ")
    else:
        print(f"Producto {nombre} no existe. ")

#Mira el inventario
def mostrar_inventario(stock):
    """Mostrar el inventario de productos"""
    print("\n------ Inventario ---")
    print("[1] Mostrar todos los productos")
    print("[2] Buscar producto por nombre")
    print("[3] Volver al menu principal")

    opcion = input("Opción: ")

    #Mostrar todos los productos
    if opcion == "1":
        if not stock:
            print("Inventario vacio. ")
            return

        print("\n--- Inventario ---")
        for nombre, datos in stock.items():
            print(f"Producto: {nombre}")
            print(f"Precio: R${datos['Precio']:.2f}")
            print(f"Cantidad: {datos['Cantidad']}")
            print("--------------------")

    #Buscar productos por nombre
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        if nombre in stock:
            print("\n--- Producto ---")
            print(f"Producto: {nombre}")
            print(f"Precio: R${stock[nombre]['Precio']:.2f}")
            print(f"Cantidad: {stock[nombre]['Cantidad']}")
        else:
            print(f"Producto {nombre} no encontrado en el inventario. ")

    elif opcion == "3":
        return
    else:
        print("Opción invalida. Por favor, seleccione una opción valida.")

#principal
def main():
    """Bucle principal del programa"""
    while True:
        stock = {}
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(stock)
        elif opcion == "2":
            actualizar_producto(stock)
        elif opcion == "3":
            eliminar_producto(stock)
        elif opcion == "4":
            mostrar_inventario(stock)
        elif opcion == "0":
            print("Saliendo del programa. ")
            break
        else:
            print("Opción invalida. ")


if __name__ == "__main__":
    main()

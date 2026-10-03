productos = [] 

while True:
    print("") # espacio
    print("") # espacio
    print("\033[34m=\033[0m"*40)
    print("\033[34mListado de productos\033[0m")
    print("\033[34m=\033[0m"*40)
    print("") # espacio
    print("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")

    print("") # espacio
    opcion = input("Seleccione una opción: (del 1 al 5): ").strip()
    print("") # espacio

    #ingresar productos
    if opcion == "1":
        print("\033[32m.\033[0m"*40)
        print("\033[32mAgregar producto \033[0m")
        print("\033[32m.\033[0m"*40)
        print("") # espacio

        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        while nombre_producto == "":
            print("El nombre del producto no puede estar vacío. Por favor, ingrese un nombre válido.")
            nombre_producto = input("Ingrese el nombre del producto: ").strip()

        categoria_producto = input("Ingrese la categoría del producto: ").strip()
        while categoria_producto == "":
            print("La categoría del producto no puede estar vacía. Por favor, ingrese una categoría válida.")
            categoria_producto = input("Ingrese la categoría del producto: ").strip()

        precio_producto = input("Ingrese el precio del producto (sin centavos): ").strip()
        while not precio_producto.isdigit():
            print("El precio del producto debe ser un número positivo. Por favor, ingrese un precio válido.")
            precio_producto = input("Ingrese el precio del producto (sin centavos): ").strip()
        precio_producto_int = int(precio_producto)

        datos_usuario = [nombre_producto, categoria_producto, precio_producto_int]
        productos.append(datos_usuario)


    # Mostrar productos
    elif opcion == "2":
        print("\033[32m.\033[0m"*40)
        print("\033[32mMostrar productos \033[0m")
        print("\033[32m.\033[0m"*40)
        print("") # espacio

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for i in range(len(productos)):
                print(f"Producto N# {i+1}\nNombre: {productos[i][0]}\nCategoría: {productos[i][1]}\nPrecio: ${productos[i][2]}")

    
    # Buscar productos
    elif opcion == "3":
        print("\033[32m.\033[0m"*40)
        print("\033[32mBuscar productos \033[0m")
        print("\033[32m.\033[0m"*40)
        print("") # espacio

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda == productos[i][0].lower():
                    print(f"Producto N# {i+1}\nNombre: {productos[i][0]}\nCategoría: {productos[i][1]}\nPrecio: ${productos[i][2]}")
                    encontrado += 1
            if encontrado == 0:
                print("Producto no encontrado.")


    # Eliminar productos           
    elif opcion == "4":
        print("\033[32m.\033[0m"*40)
        print("\033[32mEliminar producto \033[0m")
        print("\033[32m.\033[0m"*40)
        print("") # espacio
        
        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            for i in range(len(productos)):
                print(f"{i+1} {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
            id_eliminar = input("Ingrese el número del producto a eliminar: ").strip()

            while not id_eliminar.isdigit() or not (1 <= int(id_eliminar) <= len(productos)):
                print("El número ingresado no es válido. Por favor, ingrese un número válido.")
                id_eliminar = input("Ingrese el número del producto a eliminar: ").strip()

            eliminado = productos.pop(int(id_eliminar) - 1)
            print(f"Producto '{eliminado[0]}' eliminado correctamente.")

    elif opcion == "5":
        mensaje_despedida = "  Gracias por elegirnos. ¡Hasta pronto!  "
        espacio_mensaje_despedida = " " * len(mensaje_despedida)
        print(f"\033[106m{espacio_mensaje_despedida}\033[0m")
        print(f"\033[106m{mensaje_despedida}\033[0m")
        print(f"\033[106m{espacio_mensaje_despedida}\033[0m")
        print("") # espacio

        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
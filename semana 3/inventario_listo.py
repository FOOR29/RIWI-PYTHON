# ejercicio semana 3

inventario = [] # lista de diccionario

# funcion para agregar producto al inventario
def añadir_producto(inventario, producto, precio_producto, cantidad_producto):
    # validar que el producto no esté repetido
    for item in inventario:
        if producto in item:
            print(f'ERROR! El producto "{producto}" ya existe en el inventario.')
            return

    # crear un diccionario con el nombre del producto como clave y una tupla (precio, cantidad) como valor
    diccionario = {producto: (precio_producto, cantidad_producto)}
   
    # agregar el diccionario a la lista de inventario
    inventario.append(diccionario)

    print(f'El {producto} fue agregado correctamente')

# funcion para buscar un producto en el inventario
def buscarProducto(inventario, producto_buscado):
    if not inventario:
        print("Inventario vacio")
        return
   
    encontrado = False # bandera para verificar si el producto fue encontrado

    # recorrer la lista de diccionarios y buscar el producto
    for i in inventario:
        if producto_buscado in i:
            precio, cantidad = i[producto_buscado] # obtener precio y cantidad del producto
            print(f'\nProducto: {producto_buscado}')
            print(f'Precio: ${precio}')
            print(f'Cantidad disponible: {cantidad}')
            encontrado = True
            break # salir del bucle al encontrar el producto

    # si no se encontró el producto, mostrar mensaje
    if not encontrado:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')

# funcion para actualizar el precio de un producto existente
def actualizar_precio(inventario, producto_buscado, nuevo_precio):
    if not inventario:
        print("Inventario vacio")
        return

    for item in inventario:
        if producto_buscado in item:
            precio_actual, cantidad = item[producto_buscado]
            print(f'\nProducto: {producto_buscado}')
            print(f'Precio actual: ${precio_actual}')

            # actualizar el precio manteniendo la cantidad actual
            item[producto_buscado] = (nuevo_precio, cantidad)

            print(f'\nEl precio de "{producto_buscado}" fue actualizado correctamente a ${nuevo_precio}')
            break
    else:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')

# funcion para eliminar un producto del inventario
def eliminar_producto(inventario, producto_buscado):
    if not inventario:
        print("Inventario vacio")
        return

    # recorrer la lista de diccionarios para encontrar y eliminar el producto
    for item in inventario:
        if producto_buscado in item:
            inventario.remove(item)
            print(f'\nEl producto "{producto_buscado}" fue eliminado correctamente del inventario.')
            break
    else:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')

# funcion que muestra el menú de opciones
def menu():
    print('\n--INVENTARIO--')
    print('\n1) Añadir un producto')
    print('2) Consultar producto')
    print('3) Actualizar precios')
    print('4) Eliminar productos')
    print('5) Calcular valor total del inventario')
    print('6) Salir\n')

# bucle principal que muestra el menú y gestiona las opciones
while True:
    menu()
    try:
        opcion = int(input('Ingrese una opcion: '))
    except ValueError:
        print('ERROR! INGRESE UN NUMERO!')
        continue

    if opcion == 1:
        producto = input('Ingrese el nombre del producto: ').lower()
       
        # validar que el precio sea un número y positivo
        while True:
            try:
                precio_producto = float(input(f'Ingrese el precio de {producto}: '))
                break
            except ValueError:
                print('ERROR! ingrese un numero valido para el precio')

        # validar que la cantidad sea un número entero válido
        while True:
            try:
                cantidad_producto = int(input(f'Ingrese la cantidad de {producto}: '))
                break
            except ValueError:
                print('ERROR! ingrese un numero valido para la cantidad!')

        # llamar a la funcion con los parámetros
        añadir_producto(inventario, producto, precio_producto, cantidad_producto)

    elif opcion == 2:
        # si el inventario esta vacio
        if not inventario:
            print('El inventario esta vacio')
        
        else:
            # para mostrar productos disponibles
            print('\nProductos disponibles')
            for item in inventario:
                for nombre_producto in item.keys():
                    print(f'- {nombre_producto}')


            producto_buscado = input('\nIngrese el nombre del producto a buscar: ').lower()
            buscarProducto(inventario, producto_buscado)

    elif opcion == 3:
        producto_buscado = input('Ingrese el nombre del producto para actualizar su precio: ').lower()

        # validar que el nuevo precio sea un número
        while True:
            try:
                nuevo_precio = float(input('Ingrese el nuevo precio: '))
                break
            except ValueError:
                print('ERROR! Ingrese un numero valido para el precio')

        actualizar_precio(inventario, producto_buscado, nuevo_precio)

    elif opcion == 4:
        # mostrar productos antes de eliminar
        print('\nProductos disponibles')
        for item in inventario:
            for nombre_producto in item.keys():
                print(f'- {nombre_producto}')


        producto_buscado = input('\nIngrese el nombre del producto a eliminar: ').lower()
        eliminar_producto(inventario, producto_buscado)

    # calcular el valor total del inventario usando lambda
    elif opcion == 5:
        total = sum(map(lambda item: list(item.values())[0][0] * list(item.values())[0][1], inventario))
        print(f'\nEl valor total del inventario es: ${total}')

    elif opcion == 6:
        print('\nInventario cerrado!')
        break

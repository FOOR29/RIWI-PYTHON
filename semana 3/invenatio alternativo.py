# ejercicio semana 3

inventario = []  # lista de diccionario vacia

# funcion de agregar producto al inventario
def añadir_producto():

    producto = input('Ingrese el nombre del producto: ').lower()
    #validr que el precio sea positivo
    while True:
        try:
            precio_producto = float(input(f'ingrese el precio de {producto}: '))
            break
        except ValueError:
            print('ERROR! ingrese un numero valido para el precio')

    while True:
        try:
            cantidad_producto = int(input(f'Ingrese la cantidad de {producto}: '))
        except ValueError:
            print('ERROR! ingrese un numero valido para la cantidad!')
            return
        
        
    # crearbuscar diccionario con el producto
        diccionario = {producto: (precio_producto, cantidad_producto)}
    # agregar el diccionario al inventario
        inventario.append(diccionario)

        print(f'El {producto} fue agregado correctamente')
        break

# buscra producto
def buscarProducto():
    if not inventario:
        print("Inventario vacio")
        return
    producto_buscado = input('Ingrese el nombre del producto a buscar: ').lower()

    encontrado = False # verificar si lo encontramos o no

    for i in inventario:
        if producto_buscado in i:
            precio, cantidad = i[producto_buscado]  # los i eran items
            print(f'\nProducto: {producto_buscado}')
            print(f'Precio: ${precio}')
            print(f'Cantidad disponible: {cantidad}')
            encontrado = True
            break # ya se encontro

    if not encontrado:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')

# actualizar precio del productokdef 
def actualizar_precio():
    if not inventario:
        print("Inventario vacio")
        return
    producto_buscado = input('Ingrese el nombre del producto para actualizar su precio: ').lower()

    for item in inventario:
        if producto_buscado in item:
            precio_actual, cantidad = item[producto_buscado]
            print(f'\nProducto: {producto_buscado}')
            print(f'Precio actual: ${precio_actual}')

            while True:
                try:
                    nuevo_precio = float(input('Ingrese el nuevo precio: '))
                    break
                except ValueError:
                    print('ERROR! Ingrese un numero valido para el precio')

            # Actualizar el precio pero dejar la misma cantidad
            item[producto_buscado] = (nuevo_precio, cantidad)

            print(f'\nEl precio de "{producto_buscado}" fue actualizado correctamente a ${nuevo_precio}')
            break
    else:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')

# funcion para eliminart producto 
def eliminar_producto():
    if not inventario:
        print("Inventario vacio")
        return
    producto_buscado = input('Ingrese el nombre del producto a eliminar: ').lower()
# recorre la la lista de diccionarios
    for item in inventario:
        if producto_buscado in item:
            inventario.remove(item)
            print(f'\nEl producto "{producto_buscado}" fue eliminado correctamente del inventario.')
            break
    else:
        print(f'\nEl producto "{producto_buscado}" no se encuentra en el inventario.')


def menu():
    print('\n--INVENTARIO--')
    print('\n1) Añadir un producto')
    print('2) Consultar producto')
    print('3) Actualizar precios')
    print('4) Eliminar productos')
    print('5) Calcular valor total del inventario')
    print('6) Salir\n')

while True:
    menu()
    try:
        opcion = int(input('Ingrese una opcion: '))
    except ValueError:
        print('ERROR! INGRESE UN NUMERO!')

    if opcion == 1:
        añadir_producto()

    elif opcion == 2:
        buscarProducto()

    elif opcion == 3:
        actualizar_precio()

    elif opcion == 4:
        eliminar_producto()
    # sacar el valor tptal con una lambda del inventario
    elif opcion == 5:
        total = sum(map(lambda item: list(item.values())[0][0] * list(item.values())[0][1], inventario))
        print(f'\nEl valor total del inventario es: ${total}')
    elif opcion == 6:
        print('Inventario cerrado')
        break


    





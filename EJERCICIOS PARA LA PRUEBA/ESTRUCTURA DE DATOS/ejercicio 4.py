# lista de tuplas

inventario = []

nombre = input('\nIngrese el nombre del producto: ')
precio = float(input(f'Ingresa el precio de {nombre}: '))
cantidad = int(input(f'Ingrece la cantidad de {nombre}: '))

inventario.append((nombre, precio, cantidad))

for i in inventario:
    print(f'\nProducto: {inventario[0][0]}, precio: {inventario[0][1]}, cantidad: {inventario[0][2]}')

eliminar = input('\nIngrese nombre de producto a eliminar: ')

if eliminar in inventario:
    inventario.remove(([0]))
    print(inventario)




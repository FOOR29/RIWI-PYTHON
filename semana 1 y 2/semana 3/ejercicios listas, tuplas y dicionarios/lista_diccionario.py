
dicionario = []

for i in range(3):
    nombre = input('ingrese el nombre: ')
    color = input('ingrese el color: ')
    precio = input('ingrese el precio: ')
    dicionario.append({'nombre': nombre, 'color': color, 'precio': precio} )

for fruta in dicionario:
    print(f"Nombre: {fruta['nombre']}, Color: {fruta['color']}, Precio:{fruta['precio']}")

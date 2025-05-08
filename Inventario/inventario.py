
producto = {}

codigo = 000

n=int(input("cuantos productos va ingresar: "))

for i in range(n):
    nombre = input('ingrese el nombre del producto: ')
    talla = input('ingrese la talla del producto: ')
    cantidad = int(input(f'ingrese la cantidad de {nombre}: '))
    valor = float(input('ingrese el valor del producto: '))
    codigo = codigo + 1

    producto[codigo] = {
        'nombre': nombre,
        'talla' : talla,
        'cantidad' : cantidad,
        'valor' : valor
    }

for id_producto, detalles in producto.items():
    print(f"ID: {id_producto}")
    for clave, valor in detalles.items():
        print(f'{clave}: {valor}')




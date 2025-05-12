# tienda
print('\nTIENDITA LA BENDICION DE FORLAN\n')



# funciones
def costoTotal(precio, unidad):
    total = precio * unidad           # funcion para sacar total
    return total    

def descuentoAplicado(precio, cantidad, descuento):
    total = precio * cantidad
    valor_descuento = total * (descuento / 100)     # funcion para sacar descuento de varios productos
    precio_final = total - valor_descuento
    return precio_final

# funciones de errores

# para enteros
def pedirEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print('Ingrese un numero!')

# para float
def pedir_decimales(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except:
            print('Ingrese un numero!')

# para texto
def pedirTexto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() != '':
            return valor
        else:
            print('Ingresa texto por favor')

# entrada de datos
nombre_producto = pedirTexto('Ingrese el nombre del producto: ')

precio_unitario = pedir_decimales(f'Ingrese el precio de/la {nombre_producto}: ')

cant_producto = pedirEntero(f'Ingrese la cantidad de {nombre_producto} que desea llevar: ')

descuento = input('Tiene algun descuento el producto? Si/No: ').lower()

if descuento == 'no':
    sin_descuento = costoTotal(precio_unitario, cant_producto)
    print(f'\nNombre del producto: {nombre_producto}')
    print(f'Cantidad: {cant_producto}')
    print(f'Precio unitario: {precio_unitario:.1f}')
    print(f'--DESCUENTO NO APLICADO--')
    print(f'TOTAL a PAGAR: {sin_descuento:.1f}\n')

elif descuento == 'si':
    cant_descuento = int(input('De cuanto es el descuento? :'))

    if cant_descuento <= 100 and cant_descuento >= 1:
        sin_descuento = costoTotal(precio_unitario, cant_producto)
        con_descuento = descuentoAplicado(precio_unitario, cant_producto, cant_descuento)
        print(f'\nNombre del producto: {nombre_producto}')
        print(f'Cantidad: {cant_producto}')
        print(f'Precio unitario: {precio_unitario}')
        print(f'TOTAL sin DESCUENTO: {sin_descuento:.1f}')
        print(f'--DESCUENTO APLICADO--')
        print(f'TOTAL a PAGAR: {con_descuento:.1f}\n')
    else:
        print('Ingresa de 1 a 100')
else:
    print('Solo ingresa Si y No')








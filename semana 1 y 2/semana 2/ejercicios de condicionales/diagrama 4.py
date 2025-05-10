# diagrama 4

monto = input('Ingrese monto de la compra: ')

try:
    monto = float(monto)
    vip = input('¿Eres VIP? S/N: ').lower()

    if vip == 's':
        if monto >= 500:
            descuento = monto * 0.20
        else:
            descuento = monto * 0.10
    elif vip == 'n':
        if monto >= 500:
            descuento = monto * 0.05
        else:
            descuento = 0
    else:
        print('ERROR: Solo puedes ingresar S o N')
        descuento = 0

    total = monto - descuento
    print(f'Descuento aplicado: {descuento}')
    print(f'El total a pagar es: {total}')

except ValueError:
    print('ERROR Debes ingresar un número')
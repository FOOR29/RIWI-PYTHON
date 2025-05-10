# lambdas para sacar un resultado de productos

inventario = {
    'cafe': 5000,
    'azucar': 2000,
    'leche': 3500
}

calcular_valor = lambda precio, cantidad: precio * cantidad

total = sum(calcular_valor(precio, cantidad) for precio, cantidad in inventario.values())

print(f'el valor total es: {total}')





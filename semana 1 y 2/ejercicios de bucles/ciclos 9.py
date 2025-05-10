suma = 0

while True:
    numero = input('Ingresa un número o "salir": ').lower()
    
    if numero == 'salir':
        break

    numero = float(numero)
    suma += numero

print(f'La suma de los números es {suma}')
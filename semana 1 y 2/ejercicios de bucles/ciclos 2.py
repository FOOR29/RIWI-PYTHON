suma = 0

while suma < 100:
    numero = int(input('ingrese un número: '))
    suma = suma + numero
    
    if suma >= 100:
        print(f'la suma de los números es {suma}')
        break


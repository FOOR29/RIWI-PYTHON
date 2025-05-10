# pedir un numero y sumalo 
#  el programa debe detenerse cuando el usuario ingrese 0
suma = 0

while True:
    numero = int(input('ingrese un numero: '))

    suma = suma + numero

    if numero == 0:
        print(f'la suma es {suma}')
        break

    
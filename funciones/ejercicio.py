# Rey haz un menu en el cual te pida, sumar, restar, multiplicar y dividir y una opcion para salir, haz que cada funcion tenga su operador
def menu():
    print('1. sumar')
    print('2. rectar')
    print('3. multiplicar')
    print('4. dividir')
    print('5. salir')

def suma(a,b):
    total = a + b  # esta esuna forma sencilla de usar las funciones
    return total

def resta(a,b):
    total = a - b
    return total

def multiplicar(a,b):
    total = a * b
    return total

def dividir(a,b):
    total = a / b
    return total

while True:
    menu()

    opcion = int(input('elija una opcion: '))

    if 1 <= opcion <= 4:
        numero1 = int(input('ingrese un numero: '))
        numero2 = int(input('ingrese otro numero: '))

        if opcion == 1:
            print(f'La suma es: {suma(numero1,numero2)}')

        elif opcion == 2:
            print(f'La resta es: {resta(numero1,numero2)}')
        
        elif opcion == 3:
            print(f'La multiplicacion es: {multiplicar(numero1,numero2)}')
        
        elif opcion == 4:
            print(f'La division es: {dividir(numero1,numero2)}')

    elif opcion == 5:
        break

    else:
        print('Opcion no valida')

if opcion != 5:
    numero1 = int(input('ingrese su nombre: '))
    numero2 = int(input('ingrese otro numero: '))






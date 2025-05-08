# parametro predeterminado
nombre = input('ingrese su nombre: ')

def saludar(nombre = nombre):
    print(f'Hola {nombre} en que te puedo ayudar hoy')
saludar()    

# parametros y argumentos
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

def sumarNumeros (primerNumero, segundoNumero):
    total = primerNumero + segundoNumero
    return total # el return es una manera mas sencilla de mostrar en ves de print
    # print(f'la suma es: {total}')
    
print(f'la suma es: {sumarNumeros(num1, num2)}')
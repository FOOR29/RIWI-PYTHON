
#pedir 3 numreros y mostrar el mayor de ellos

numero1 = int(input('ingrese un numero: '))
numero2 = int(input('ingrese otro numero: '))
numero3 = int(input('ingrese el ultimo numero: '))

if numero1 > numero2 and numero1 > numero3 :
    print(f'el numero {numero1} es mayor a {numero2} y numero {numero3}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'el numero {numero2} es mayor a {numero1} y numero {numero3}')
else:
    print(f'el numero {numero3} es mayor a {numero2} y numero {numero1}')





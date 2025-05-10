
# compara dos numeros 

numero1 = int(input('ingrese un numero: '))
numero2 = int(input('ingrese otro numero: '))

if numero1 == numero2:
    print('los numeros son iguales')
elif numero1 > numero2:
    print(f'el numero {numero1} es mayor a {numero2}')
else:
    print(f'el numero {numero2} es mayor a {numero1}')
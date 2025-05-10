numero = int(input('ingresa un número: '))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i
    
print(f'el factorial de {numero} es {factorial}') 
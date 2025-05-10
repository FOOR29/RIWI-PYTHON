
contador = 0

for i in range(1, 11):
    numero = int(input('ingresa un número: '))
    
    if numero > 0:
        contador += 1

print(f'hay {contador} positivos')
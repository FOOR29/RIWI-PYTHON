
contador = 0

num_positivos = 0

while contador < 5:
    numero = int(input('ingresa un numero: '))
    if numero > 0:
        num_positivos += 1
    
    contador = contador + 1

print(f'hay {num_positivos} positivos')    







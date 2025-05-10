inicio = int(input('ingresa el número inicial: '))
final = int(input('ingresa número final: '))

contador = 0

for i in range(inicio, final + 1):
    if i % 2 == 0:
        contador = contador + 1
    
print(f'hay {contador} pares')
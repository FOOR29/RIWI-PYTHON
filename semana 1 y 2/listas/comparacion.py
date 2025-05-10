nota = [1, 3, 6, 3, 10, 6, 5]
contador = 0

nota_minima = int(input('nota minima: '))


for notas in nota:
    if notas > nota_minima:
        contador = contador + 1

print(f'aprobaron: {contador}')        




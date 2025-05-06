numeros = ([(1, 3), (73, 66)], [(2, 44), (89, 99)], [(10, 11), (45, 33)])


numeros[2][1] = (45, 444) # como la tuplas no se puede modificar se reemplaza la tupla

for nume1, nume2 in numeros:
    print(nume1, nume2)



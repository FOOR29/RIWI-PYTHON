# Crea una tupla que contenga 3 listas, cada lista a su vez debe tener dos tuplas, cada tupla debe tener 2 elementos c-u, 
# cambia el segundo elemento de la segunda tupla, de la tercera lista y luego imprime estructura final


tupla_1 = ([(1,2), (3,4)], [(46,90),(70,55)], [(5,7),(87,98)])

tupla_1[2][1] = (87, 400)

for nume1, nume2 in tupla_1:
    print(nume1, nume2)



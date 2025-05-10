# definir un numero secreto por ejemplo 5
# pide al usuario que adivine el numero hasta que lo acierte

numero_secreto = 14

while True:
    numero = int(input('adivina mi numero del 1 al 20: '))

    if numero == numero_secreto:
        print('muy bien! era el 14')
        break
    else:
        print('sigue intentando papa')
        






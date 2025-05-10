# diagrama 3

dia = input('¿El día es laborable? S/N: ').lower()

try:
    if dia == 's':
        hora = int(input('Ingresa la hora (0-23): '))

        if hora < 0 or hora > 23:
            print('Hora inválida. Debe estar entre 0 y 23.')
        elif (7 <= hora <= 9) or (17 <= hora <= 19):
            print('Hora pico')
        else:
            print('Hora normal')

    elif dia == 'n':
        print('Fin de semana')

    else:
        print('Error: debes ingresar solo "S" o "N"')
        
except ValueError:
    print('Error: debes ingresar solo números enteros en la hora.')
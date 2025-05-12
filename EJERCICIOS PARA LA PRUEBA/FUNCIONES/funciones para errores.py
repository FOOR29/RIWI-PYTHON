

# para enteros
def pedirEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print('Ingrese un numero!')


# para float
def pedir_decimales(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except:
            print('Ingrese un numero!')


# para texto
def pedirTexto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() != '':
            return valor
        else:
            print('Ingresa texto por favor')













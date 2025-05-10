# definir una contraseña ya definida
# pide al usuario que ingrese una hasta que la escriba correctamente

contraseña_correcta = 'pepito1234'

while True:
    contraseña = input('ingresa tu contraseña: ')

    if contraseña == contraseña_correcta:
        print('CONTRASEÑA CORRECTA!')
    else:
        print('incorrecta, prueba de nuevo')






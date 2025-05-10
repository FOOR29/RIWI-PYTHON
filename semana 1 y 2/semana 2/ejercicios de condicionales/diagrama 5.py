
#Diagrama 5
print('Cree una contraseña, almenos 8 caracteres y @\n')

contraseña = input('Ingresar: ')

if len(contraseña) >= 8 and '@' in contraseña:
    print('contraseña valida')
elif len(contraseña) < 8:
    print('muy corta')
else:
    print('falto el @')
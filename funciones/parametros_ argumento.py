# parametro y argumentos
# las funciones pueden aceptar parametros (num1, num2) que son variables 
# que pasan a la funcion cuando se llama num1 + num2
# esos parametros se convierten en variables locales dentro de la funcion


def sumarNumeros (num1, num2):
    total = num1 + num2
    print(f'el resultado es {total}')

sumarNumeros(5,6)
sumarNumeros(8,3)
sumarNumeros(89,3)

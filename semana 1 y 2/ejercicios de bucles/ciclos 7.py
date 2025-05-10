palabra = input('ingresa una palabra: ')
contador = 0


for letra in palabra:
    if letra == 'a':
        contador = contador + 1

print(f'la letra "a" aparece {contador} veces') 
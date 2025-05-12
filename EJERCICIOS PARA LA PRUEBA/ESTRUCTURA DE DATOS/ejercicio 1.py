
lista = []

for i in range(5):
    cancion = input('Ingresa un tema: ')
    lista.append(cancion)

print(f'\nHay {len(lista)} temas\n')
for tema in lista:
    print(f'- {tema}')





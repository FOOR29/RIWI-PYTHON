colores = (['rojo', 'verde'], ['amarillo', 'naranja'], ['negro', 'azul'])

colores[1][0]= 'blanco'  # para cambiar valor dentro de una tupla de listas
                         # el [1] es el indice de la listas en si ej: ['amarillo', 'naranja']
                         # el [0] es el indice dentro de la lista 1

for color1, color2 in colores:
    print(f'{color1} {color2}')


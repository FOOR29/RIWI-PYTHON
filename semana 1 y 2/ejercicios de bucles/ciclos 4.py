secreto = 8
contador = 0

while contador < 5:
    numero = int(input('adivina el número del 1 al 10: '))
    contador = contador + 1
    
    if numero == secreto:
        print('Lo adivinaste!')
        break  
    if contador == 5:
        print('Fallaste')
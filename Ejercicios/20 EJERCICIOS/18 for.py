# pide al usuario un numero N y muestra la suma de los numeros del 1 al N

numero = int(input('ingrese un numero: '))
contador = 0
for i in range(numero+1):
    contador += i
print(contador)
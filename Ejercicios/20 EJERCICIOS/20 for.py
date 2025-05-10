# Pide al usuario un número y calcula su factorial usando un ciclo para.

numero = int(input('ingresa un numero: '))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i 

print(f"El factorial de {numero} es: {factorial}")




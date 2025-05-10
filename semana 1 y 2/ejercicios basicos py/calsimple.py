def calcular(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    if numero2 != 0:
        division = numero1 / numero2
    else:
        division = "Error: división por cero"

    # Mostrar los resultados
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

# Llamada a la función con dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
calcular(numero1, numero2)

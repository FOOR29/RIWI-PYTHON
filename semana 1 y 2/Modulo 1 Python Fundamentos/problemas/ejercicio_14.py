print("validar si el primero es mayor o no")

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if numero_1 > numero_2:
    print(f"si, el {numero_1} es mayor")
elif numero_1 < numero_2:
    print(f"no es mayor, el numero {numero_1} es mayor")
else:
    print("ambos numeros son iguales")
 
# el if para (si pasa esto...)
# el elif es para (si no,  pero pasa estp otro)
#el else por si ninguna de las funciuones no se cumplen
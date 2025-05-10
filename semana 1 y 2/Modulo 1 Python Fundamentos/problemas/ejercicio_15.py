print("validar si el primero es menor o igual")

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if numero_1 < numero_2:
    print(f"si el {numero_1} es menor a {numero_2}")
elif numero_1 > numero_2:
    print(f"no, el {numero_1} es mayor que {numero_2}")
else:
    print("ambos numeros son iguales")


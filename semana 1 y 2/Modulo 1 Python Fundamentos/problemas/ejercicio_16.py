print("validar si los dos numeros son mayor que 10")

numero_1 = int(input("ingrese el primer numero: "))
numero_2 = int(input("ingrese el segundo numero: "))

if numero_1 > 10 and numero_2 > 10:
    print(f"si {numero_1} y {numero_2} son mayores a 10")
elif numero_1 <= 10 and numero_2 <= 10:
    print("ambos numeros son menores o iguales a 10")
else:
    print("uno es menor que el otro")

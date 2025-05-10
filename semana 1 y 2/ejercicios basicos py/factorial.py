n = int(input("Ingresa un numero positivo: "))

if n < 0:
    print("El numero debe ser positivo")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

        if factorial > 9999999999:
            print("El resultado excede los 10 digitos permitidos")
            break
    else:
        print(f"El factorial de {n} es {factorial}")












#n=int(input())
#sum=0
#m=0
#factorial=1

#for i in range(1, n + 1):
#    factorial *= i
#    sum=factorial-m
#    print(sum)

#numero1 = float(input("Ingresa el primer número: "))
#numero2 = float(input("Ingresa el segundo número: "))
#calcular(numero1, numero2)


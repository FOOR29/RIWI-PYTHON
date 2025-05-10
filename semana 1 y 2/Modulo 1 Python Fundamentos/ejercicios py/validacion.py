while True:
    usuario = input("ingrese su usuario ")
    edad = int(input("ingrese su edad: "))

    if usuario == "palabra" or edad >= 18:
        print("puedes ingresar")
    else :
        print("no puedes malparido")
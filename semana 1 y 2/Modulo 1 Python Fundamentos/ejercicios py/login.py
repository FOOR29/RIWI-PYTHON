password = "123"
username = "forlan"

##sistema de login



while True:
    custom_username = input("ingrese su usuario: ")
    custom_password = input("ingrese su contraseña: ")
    if (custom_password == password) and (custom_username == username) :
        print("login exitoso")
        break
    else:
        print("login fallido")
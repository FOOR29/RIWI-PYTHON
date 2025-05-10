 # diagrama 2
try:
    edad = int(input('Cual es tu edad: '))

    if edad < 18:
        print('eres menor de edad')
    elif edad >= 18 and edad <= 30:
        print('eres adulto mayor')
    elif edad >= 31 and edad <= 65:
        print('eres adulto maduro') 
    elif edad > 65:
        print('eres adulto mayor') 
      
except:
    print('introduce un numero')
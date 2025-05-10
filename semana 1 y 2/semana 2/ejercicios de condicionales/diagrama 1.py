# diagrama 1 
try:
    numero = int(input('introduce un número: '))
except:
    print('introduce un numero')
    
if numero > 0:
    print('es positivo')
if numero < 0:
    print('es negativo')
if numero == 0:
    print('es cero')       
elif numero != 0 and numero % 2 == 0:
    print('y el números es par')
else:
    print('y el número es impar') 
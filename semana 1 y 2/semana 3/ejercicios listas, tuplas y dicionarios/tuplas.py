
frutas = []

for i in range(3):
    nombre = input('ingrese nombre: ')
    color = input('ingrese el color: ')
    precio = float(input('ingrese el precio: '))
    frutas.append((nombre, color, precio))

for fruta in frutas:
    print(f'nombre: {fruta[0]}, color: {fruta[1]}, precio: {fruta[2]}')




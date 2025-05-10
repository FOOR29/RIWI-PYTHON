
frutas = []

for i in range(3):
    nombre = input('ingrese el nombre: ')
    color = input('ingrese el color: ')
    precio = float(input('ingrese el precio: '))
    frutas.append([nombre, color, precio])

for fruta in frutas:
    print(f"Nombre: {fruta[0]}, Color: {fruta[1]}, Precio:{fruta[2]}")




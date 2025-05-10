def obtener_nombre_producto():
    return input("Ingrese el nombre del producto: ")

def obtener_precio_unitario():
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio <=0:
                print("El precio debe ser numero positivo.")
                continue
            return precio
        except ValueError:
            print("Por favor ingrese un numero valido.")

def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
            if cantidad <=0:
                print("La cantidad debe ser un numero entero positivo.")
                continue
            return cantidad
        except ValueError:
            print("Porfavor ingrese un numero valido.")

def obtener_descuento():
    while True:
        try:
            descuento = float(input("Ingrese el procentaje de descuento (0-100): "))
            if 0 <= descuento <= 100:
                break
            else:
                print("El descuento debe ser entre 0 y 100.")
        except ValueError:
            print("Por favor ingresa un numero valido.")

def calcular_total(precio, cantidad, descuento):
subtotal = precio_unitario * cantidad
total_descuento = subtotal * (descuento / 100)
total = subtotal -total_descuento

#print(f"El costo total de la compra de {nombre_producto} es: ${total:.2f}")
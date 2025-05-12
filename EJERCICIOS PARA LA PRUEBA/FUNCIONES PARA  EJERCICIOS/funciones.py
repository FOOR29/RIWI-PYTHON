
# funciones de errores

# para enteros
def pedirEntero(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print('Ingrese un numero!')

# para float
def pedir_decimales(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except:
                print('Ingrese un numero!')


# para texto
def pedirTexto(mensaje):
        while True:
            valor = input(mensaje)
            if valor.strip() != '':
                return valor
            else:
                print('Ingresa texto por favor')


# funciones
def costoTotal(precio, unidad):
        total = precio * unidad           # funcion para sacar total
        return total    

def descuentoAplicado(precio, cantidad, descuento):
        total = precio * cantidad
        valor_descuento = total * (descuento / 100)     # funcion para sacar descuento de varios productos
        precio_final = total - valor_descuento
        return precio_final




# para agregar producto

def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


# para actualizar precio

def actualizar_precio(inventario, nombre, nuevo_precio):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if nuevo_precio > 0:
                producto["precio"] = nuevo_precio
                return True
            else:
                return False
    return None

# para eliminar producto
def eliminar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            return True
    return False


# calcular total de un inventario
def calcular_valor_total(inventario):
    total = 0
    for producto in inventario:
        total += producto["precio"] * producto["cantidad"]
    return round(total, 2)



def main():
    inventario = []

    # Añadir 5 productos iniciales
    agregar_producto(inventario, "Café", 5.0, 10)
    agregar_producto(inventario, "Azúcar", 2.5, 20)
    agregar_producto(inventario, "Harina", 3.0, 15)
    agregar_producto(inventario, "Aceite", 7.0, 8)
    agregar_producto(inventario, "Sal", 1.5, 25)

    # Aquí puedes probar las funciones
    # Ejemplo
    print(consultar_producto(inventario, "Café"))
    actualizar_precio(inventario, "Café", 6.0)
    eliminar_producto(inventario, "Azúcar")
    total = calcular_valor_total(inventario)
    print(f"Valor total del inventario: ${total}")
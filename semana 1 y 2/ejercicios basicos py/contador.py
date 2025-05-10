def obtener_dato_numerico(mensaje, tipo="float"):
    while True:
        try:
            dato = input(mensaje)
            if tipo == "float":
                dato = float(dato)
            elif tipo == "int":
                dato = int(dato)
            
            if dato < 0:
                print("El valor debe ser un número positivo. Inténtalo de nuevo.")
            else:
                return dato
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def calcular_costo_total(precio_unitario, cantidad, descuento):
    # Calcular el costo sin descuento
    costo_sin_descuento = precio_unitario * cantidad
    # Calcular el monto del descuento
    monto_descuento = costo_sin_descuento * (descuento / 100)
    # Calcular el costo total después de aplicar el descuento
    costo_total = costo_sin_descuento - monto_descuento
    return costo_total

def main():
    print("Bienvenido a la tienda en línea")
    
    # Solicitar los datos del usuario
    nombre_producto = input("Ingresa el nombre del producto: ")
    precio_unitario = obtener_dato_numerico("Ingresa el precio unitario del producto: $", "float")
    cantidad = obtener_dato_numerico("Ingresa la cantidad de productos adquiridos: ", "int")
    descuento = obtener_dato_numerico("Ingresa el porcentaje de descuento (0 a 100): ", "float")
    
    # Validar que el descuento esté dentro del rango permitido
    if descuento < 0 or descuento > 100:
        print("El descuento debe estar entre 0 y 100%. El descuento será considerado como 0%.")
        descuento = 0
    
    # Calcular el costo total
    costo_total = calcular_costo_total(precio_unitario, cantidad, descuento)
    
    # Mostrar el resultado
    print(f"\nResumen de la compra:")
    print(f"Producto: {nombre_producto}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Descuento: {descuento}%")
    print(f"Costo total: ${costo_total:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
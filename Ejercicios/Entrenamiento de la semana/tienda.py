# entrada de datos basicos

print("Bienvenido a la tienda DOÑA JUANA\n")
nombre = input('Cual es tu nombre?: \n')
print (f"Es un placer tenerte por aqui {nombre}")
nombre_producto = input("Que producto desea llevar hoy?: ")

#validacion de datos
while True :
    try:
        precio_unitario = int(input("Ingrese el precio unitario: "))
        cantidad_producto = int(input("Ingrese porfavor la cantidad de producto que desea adquirir en su compra: "))
        porcentaje_descuento = int(input("Ingrese porfavor el descuento que tiene el producto(En caso de que no disponga digite 0):" ))
        costo_sin_descuento = (precio_unitario )* (cantidad_producto)
    #Valida que los datos ingresados son numeros 
        if (precio_unitario > 0 ) and (cantidad_producto > 0 ) and (porcentaje_descuento <= 100) and (porcentaje_descuento >= 1):
            costo_descuento = (costo_sin_descuento) * (porcentaje_descuento) / 100
            print ("El producto que desea llevar es",nombre_producto)
            print (f"El total con el descuento aplicado es: {costo_sin_descuento - costo_descuento:.2f}")
        else:
            costo_sin_descuento = (precio_unitario ) * (cantidad_producto)
            print ("El producto que desea llevar es",nombre_producto)
            print (f"El total de su compra es:{costo_sin_descuento:.2f}")
        break
    except:
        print("¡Hiciste algo que no se esperaba!,(DIGITE PORFAVOR SOLO NUMEROS EN PRECIO UNITARIO Y CANTIDAD DE PRODUCTOS.)")

# mensaje final
print ("¡Gracias por su compra!")
print ("Esperamos su pronto regreso:)")
print ("¡Que tenga un excelente dia!")
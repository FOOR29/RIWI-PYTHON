# ENTRADA DE DATOS BASICOS

print("Hola bienvenido a la tienda Doña juana!!\n")
nombre = input('Cual es tu nombre?: \n')
print (f"Es un placer tenerte por aqui {nombre}")

# entrada de productos

producto = input("Que producto desea llevar hoy?: ")
precio = float(input(f"muy bien, que precio tiene la {producto}? (ingrese valores numericos): "))
unidades = int(input("cuántas unidades desea llevar: "))
descuento = input(f"el {producto} tiene algún descuento? Si/No: ").lower()

# proceso de de descuento y numero de pedidos

precio_total = precio * unidades

if descuento == "si":
    porcentaje_descuento = float(input("de cuánto es el descuento?: "))  
    descuento_aplicado = (precio_total * porcentaje_descuento)/100  # proceso de descuento
    precio_final = precio_total - descuento_aplicado

else:
    precio_final = precio_total

# aqui cree una tipo factura electronica

print("Costo total de la compra\n")
print(f"precio del {producto}: {precio}")
print(f"cantidad de unidades: {unidades}")
if descuento == "si":
    print(f"precio sin descuento: {precio_total}")
    print(f"precio con descuento: {precio_final}")
elif descuento == "no":
    print("descuento no aplicado")
    print(f"monto a pagar: {precio_final}")



#listas o arreglos

dias = ["lunes","martes","miercoles","jueves"]
print(dias[0])
print(dias[1])
print(dias[2])
print(dias[3])
print(len(dias))
print(dias[1:])

# objetos o diccionarios

coder = {
    "nombre": "forlan",
    "apellido": "ordoñez",
    "estatura": "1.77",
}

print(coder["nombre"])

coder["fecha de nacimiento"] = "12-12-2001"
print(coder)

coder.pop("apellido")
print(coder)
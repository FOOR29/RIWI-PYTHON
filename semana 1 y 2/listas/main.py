
lista = [
    ("manzana",100),
    ("pera ",200),
    ("mango",300)
]
eliminar = input("cual deseas eliminar: ")
for i in range(len(lista)):
    if eliminar=="manzana":
        elim1 = lista.pop(0)
    elif eliminar == "pera":
        elim2 = lista.pop(1)
    elif eliminar == "mango":
        elim3 = lista.pop(2)
print(lista)



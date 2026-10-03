#remove() elimina el primer elemento que coincida con el valor especificado. Si el valor no se encuentra, se genera un ValueError.
productos = ["pan", "leche", "queso"]
productos.remove("pan")

print(productos)  
# Salida: ["leche", "queso"]



#clear() elimina todos los elementos de la lista, dejándola vacía.
mi_lista = [1, 2, 3, 4, 5]
mi_lista.clear()

print(mi_lista) # salida: []
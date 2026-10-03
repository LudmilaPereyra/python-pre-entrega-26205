productos = ["manzanas", "piñas", "bananas", "uvas"]
for producto in productos:
    print("Producto disponible:", producto)


palabra = "Hola"
for letra in palabra:
    print("Letra:", letra)


#Uso de break en bucles for
productos = ["P001", "P002", "P003", "P004", "P005"]
producto_a_buscar = "P003"
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto encontrado:", producto)
        break
    print("Buscando...")
print("Fin de la búsqueda.")


#Filtrado de nombres
usuarios = ["Ana", "Luis", "Andrés", "María", "Alejandro", "Lucía"]
letra_buscada = "A"

for nombre in usuarios:
    if nombre.startswith(letra_buscada):
        print(f"Nombre que empieza con '{letra_buscada}': {nombre}")
# Inicializamos el contador en 0
intentos = 0
# Establecemos el máximo de intentos permitidos
max_intentos = 3
# Usamos un bucle que se detendrá si el usuario
# ingresa un nombre válido o si se agotan los intentos
while intentos < max_intentos:
   # Solicitamos al usuario que ingrese su nombre
   nombre = input("Ingresá tu nombre de usuario: ").strip()
   # Verificamos si el nombre ingresado no está vacío
   if nombre != "":
       print(f"Bienvenido/a, {nombre}!")  # Mensaje de éxito
       break  # Salimos del bucle si se ingresa un nombre válido
   else:
       print("El nombre no puede estar vacío. Intentá de nuevo.")
   # Incrementamos el contador de intentos
   intentos += 1
# Verificamos si se agotaron los intentos
if intentos == max_intentos:
   print("Se agotaron los intentos. Intente más tarde.")
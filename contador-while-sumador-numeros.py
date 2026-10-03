numero = 0
print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.")
suma = 0
while True:
   # Solicitamos al usuario un número
   numero = int(input("Ingresá un número: "))
   # Verificamos si el número es negativo
   if numero < 0:
       print("El número es negativo, se ignora. Intentá de nuevo.")
       continue  
   if numero == 0:
       break
   suma += numero
print(f"La suma de los números positivos es: {suma}")
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
correoElectronico = input("Ingrese su correo electrónico ")

if nombre != "" and apellido != "" and edad != "" and correoElectronico != "" and int(edad) >= 18:   
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Correo electrónico:", correoElectronico)
else:
    print("Error: Todos los campos son obligatorios y la edad debe ser un número mayor o igual a 18.")
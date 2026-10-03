nombre = input("Ingrese su nombre: ").strip().upper()
apellido = input("Ingrese su apellido: ").strip().upper()
email = input("Ingrese su correo electrónico: ").strip()
edad = int(input("Ingrese su edad: "))

if nombre.isalpha() and apellido.isalpha():
    if edad >= 18:
        if "@" in email and "." in email:
            print(f"Bienvenido {nombre} {apellido}, su correo electrónico es {email} y su edad {edad}.")
        else:
            print("Lo siento, debe ingresar un correo electrónico válido.")
    else:
        print("Lo siento, debe ser mayor de edad para registrarse.")
else:
    print("Lo siento, el nombre y apellido deben contener solo letras.")
nota = int(input("ingresa una nota (0 a 100)"))
if nota < 0:
    print("La nota no puede ser menor a 0")
else:
    if nota < 60:
        print("Reprobado")
    else: 
        if nota < 80:
            print("Aprobado")
        else:
            if nota < 90:
                print("Muy bien")
            else:
                if nota <= 100:
                    print("Excelente")
                else:
                    print("La nota no puede ser mayor a 100")
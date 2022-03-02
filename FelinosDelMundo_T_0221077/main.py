from Clases.Felidae import *


nombreUsuario = input("Ingrese su nombre: ")

respuesta = 0
while respuesta != "S":
    print("---------------------------------------------")
    print("Bienvenido a la base de datos del zoológico\t\n",nombreUsuario)
    print("\nSeleccione el animal que desee consultar")
    print("1.- Perro\n\t")
    print("2.- León\n\t")
    print("3.- Oso\n\t")
    print("4.- Tortuga\n\t")
    print("5.- Cebra\n\t")
    print("Presione <S> para salir de la base de datos del zoológico")
    respuesta = input()

    if respuesta == "1":
        perro1 = perro("Cachorro Husky", "Bosque Templado", "Padre Husky", "Madre Husky","Está alimetado", 10, 80,"Zona de animales domesticos", "De 7.5 a 180 km/h")
        perro1.mostrarDatosPerro()
        respuesta = 0
        while respuesta != "S":
            print("---------------------------------------------")
            print("Seleccione lo que desee hacer con el animal")
            print("1.- Alimentar\n\t")
            print("2.- Sedar\n\t")
            print("3.- Transladar\n\t")
            print("4.- Estado médico\n\t")
            print("Presione <S> para salir")
            respuesta = input()

            if respuesta == "1":
                print(perro1.alimentar())

            elif respuesta == "2":
                print(perro1.sedar())

            elif respuesta == "3":
                print(perro1.transladar())

            elif respuesta == "4":
                print(perro1.revisiónMP())




    elif respuesta == "2":
        león1 = león("León del Congo", "Sabana", "Padre león del Congo", "Madre león del Congo", "NO está alimetado", 142, 125,"Zona de animales peligrosos", "55 km/h")

        león1.mostrarDatosLeón()
        respuesta = 0
        while respuesta != "S":
            print("-------------------------------")
            print("Seleccione lo que desee hacer con el animal")
            print("1.- Alimentar\n\t")
            print("2.- Sedar\n\t")
            print("3.- Transladar\n\t")
            print("4.- Estado médico\n\t")
            print("Presione <S> para salir")
            respuesta = input()

            if respuesta == "1":
                print(león1.alimentar())

            elif respuesta == "2":
                print(león1.sedar())

            elif respuesta == "3":
                print(león1.transladar())

            elif respuesta == "4":
                print(león1.revisiónMP())




    elif respuesta == "3":
        oso1 = oso("Oso Pardo", "Selva Tropical", "Padre Oso Pardo", "Madre Oso Pardo", "NO está alimetado", 200, 230,"Zona de animales peligrosos", "56 km/h")

        oso1.mostrarDatosOso()
        respuesta = 0
        while respuesta != "S":
            print("-------------------------------")
            print("Seleccione lo que desee hacer con el animal")
            print("1.- Alimentar\n\t")
            print("2.- Sedar\n\t")
            print("3.- Transladar\n\t")
            print("4.- Estado médico\n\t")
            print("Presione <S> para salir")
            respuesta = input()

            if respuesta == "1":
                print(oso1.alimentar())

            elif respuesta == "2":
                print(oso1.sedar())

            elif respuesta == "3":
                print(oso1.transladar())

            elif respuesta == "4":
                print(oso1.revisiónMC())



    elif respuesta == "4":
        tortuga1 = tortuga("Tortuga de oreja amarilla", "Pantano", "Padre Tortuga de oreja amarilla", "Madre Tortuga de oreja amarilla", "Está alimetada", 1, 4,"Zona del lago", "2 km/h")

        tortuga1.mostrarDatosTortuga()
        respuesta = 0
        while respuesta != "S":
            print("-------------------------------")
            print("Seleccione lo que desee hacer con el animal")
            print("1.- Alimentar\n\t")
            print("2.- Sedar\n\t")
            print("3.- Transladar\n\t")
            print("4.- Estado médico\n\t")
            print("Presione <S> para salir")
            respuesta = input()

            if respuesta == "1":
                print(tortuga1.alimentar())

            elif respuesta == "2":
                print(tortuga1.sedar())

            elif respuesta == "3":
                print(tortuga1.transladar())

            elif respuesta == "4":
                print(tortuga1.revisiónMP())




    elif respuesta == "5":
        cebra1 = cebra("Cebra de montaña", "Pastizal", "Padre Cebra de montaña", "Madre Cebra de montaña", "NO está alimetado", 176, 200,"Zona de animales de montaña", "65 km/h")

        cebra1.mostrarDatosCebra()
        respuesta = 0
        while respuesta != "S":
            print("-------------------------------")
            print("Seleccione lo que desee hacer con el animal")
            print("1.- Alimentar\n\t")
            print("2.- Sedar\n\t")
            print("3.- Transladar\n\t")
            print("4.- Estado médico\n\t")
            print("Presione <S> para salir")
            respuesta = input()

            if respuesta == "1":
                print(cebra1.alimentar())

            elif respuesta == "2":
                print(cebra1.sedar())

            elif respuesta == "3":
                print(cebra1.transladar())

            elif respuesta == "4":
                print(cebra1.revisiónMC())



from CFelidae import *


nombreUsuario = input("Ingrese su nombre: ")

respuesta = 0
while respuesta != "S":
    print("---------------------------------------------")
    print("Bienvenido a la base de datos del zoológico\t\n",nombreUsuario)
    print("\nSeleccione el animal que desee consultar")
    print("1.- Tigre\n\t")
    print("2.- León\n\t")
    print("3.- Jaguar\n\t")
    print("4.- Puma\n\t")
    print("5.- Leopardo\n\t")
    print("Presione <S> para salir de la base de datos del zoológico")
    respuesta = input()

    if respuesta == "1":
        tigre1 = tigre("Tigre de Bengala (Macho)", "Selva tropical", "Padre tigre de Bengala", "Madre tigre de Bengala","Está alimetado", 180, 260,"Zona de animales peligrosos", "De 49 a 65 km/h")
        tigre1.mostrarDatosTigre()
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
                print(tigre1.alimentar())

            elif respuesta == "2":
                print(tigre1.sedar())

            elif respuesta == "3":
                print(tigre1.transladar())

            elif respuesta == "4":
                print(tigre1.revisiónMP())




    elif respuesta == "2":
        león1 = león("León del Congo (Macho)", "Sabana", "Padre león del Congo", "Madre león del Congo", "NO está alimetado", 142, 125,"Zona de animales peligrosos", "55 km/h")

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
        jaguar1= jaguar("Jaguar (Hembra)", "Selva Tropical", "Padre Jaguar", "Madre Jaguar", "NO está alimetada", 80, 150,"Zona de animales peligrosos", "80 km/h")

        jaguar1.mostrarDatosJaguar()
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
                print(jaguar1.alimentar())

            elif respuesta == "2":
                print(jaguar1.sedar())

            elif respuesta == "3":
                print(jaguar1.transladar())

            elif respuesta == "4":
                print(jaguar1.revisiónMC())



    elif respuesta == "4":
        puma1 = puma("Puma (Hembra)", "Selva Húmeda", "Padre Puma ", "Madre Puma ", "Está alimetada", 75, 42,"Zona de animales peligrosos","80 km/h")
        puma1.mostrarDatosPuma()
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
                print(puma1.alimentar())

            elif respuesta == "2":
                print(puma1.sedar())

            elif respuesta == "3":
                print(puma1.transladar())

            elif respuesta == "4":
                print(puma1.revisiónMP())




    elif respuesta == "5":
        leopardo1 = leopardo("Leopardo (Macho)", "Selva tropical y montaña", "Padre Leopardo", "Madre Leopardo", "NO está alimetado", 90, 91,"Zona de animales de montaña", "58 km/h")

        leopardo1.mostrarDatosLeopardo()
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
                print(leopardo1.alimentar())

            elif respuesta == "2":
                print(leopardo1.sedar())

            elif respuesta == "3":
                print(leopardo1.transladar())

            elif respuesta == "4":
                print(leopardo1.revisiónMC())

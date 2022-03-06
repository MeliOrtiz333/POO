from Clases import *


nom_user = input("Ingrese su nombre: \t")
r = 0

while r != "S":
    print("\n¡Bienvenido al menú de la flota naval!: \t\t", nom_user)
    print("Seleccione el barco de su preferencia\t ")
    print("1.- Acorazado")
    print("2.- Destructor")
    print("3.- Crucero")
    print("Pulse <S> para salir")
    r = input()


    if r == "1":


        acorazado1 = Acorazado("Nombre", "Tripulación","Armamento primario y secundario", "Desplegables", "Coordenadas", "Cantidad de Combustible", "Velocidad")
        acorazado1.mostrarDatosAcorazado()

        respuesta = 0
        while respuesta != "R":
            print("---------------------------------------------")
            print("Seleccione lo que desee hacer con el barco")
            print("1.- Cambiar la velocidad\n\t")
            print("2.- Apagar o prender motores\n\t")
            print("3.- Sacar armamento\n\t")
            print("4.- Consulte las coordenadas\n\t")
            print("5.- Consulte la cantidad de combustible\n\t")
            print("Presione <R> para regresar al menu de barcos\n\t")
            print("---------------------------------------------")
            respuesta = input()

            if respuesta == "1":
                print(acorazado1.VelocidadAcorazado())

            elif respuesta == "2":
                print(acorazado1.MotoresAcorazado())

            elif respuesta =="3":
                print(acorazado1.DispararArmaAcorazado())

            elif respuesta == "4":
                print(acorazado1.coordenadasAcorazado())

            elif respuesta == "5":
                print(acorazado1.CantidadCombustibleAcorazado())


    elif r == "2":



        destructor1 = Destructor("Nombre", "Tripulación","Armamento primario y secundario", "Desplegables", "Coordenadas", "Cantidad de Combustible", "Velocidad")
        destructor1.mostrarDatosDestructor()

        respuesta = 0
        while respuesta != "R":
            print("---------------------------------------------")
            print("Seleccione lo que desee hacer con el barco")
            print("1.- Cambiar la velocidad\n\t")
            print("2.- Apagar o prender motores\n\t")
            print("3.- Sacar armamento\n\t")
            print("4.- Consulte las coordenadas\n\t")
            print("5.- Consulte la cantidad de combustible\n\t")
            print("Presione <R> para regresar al menu de barcos\n\t")
            print("---------------------------------------------")
            respuesta = input()

            if respuesta == "1":
                print(destructor1.VelocidadDestructor())

            elif respuesta == "2":
                print(destructor1.MotoresDestructor())

            elif respuesta =="3":
                print(destructor1.DispararArmaDestructor())

            elif respuesta == "4":
                print(destructor1.coordenadasDestructor())

            elif respuesta == "5":
                print(destructor1.CantidadCombustibleDestructor())


    elif r == "3":



        crucero1 = Crucero("Nombre", "Tripulación","Armamento primario y secundario", "Desplegables", "Coordenadas", "Cantidad de Combustible", "Velocidad")
        crucero1.mostrarDatosCrucero()

        respuesta = 0
        while respuesta != "R":
            print("---------------------------------------------")
            print("Seleccione lo que desee hacer con el barco")
            print("1.- Cambiar la velocidad\n\t")
            print("2.- Apagar o prender motores\n\t")
            print("3.- Sacar armamento\n\t")
            print("4.- Consulte las coordenadas\n\t")
            print("5.- Consulte la cantidad de combustible\n\t")
            print("Presione <R> para regresar al menu de barcos\n\t")
            print("---------------------------------------------")
            respuesta = input()

            if respuesta == "1":
                print(crucero1.VelocidadCrucero())

            elif respuesta == "2":
                print(crucero1.MotoresCrucero())

            elif respuesta =="3":
                print(crucero1.DispararArmaCrucero())

            elif respuesta == "4":
                print(crucero1.coordenadasCrucero())

            elif respuesta == "5":
                print(crucero1.CantidadCombustibleCrucero())

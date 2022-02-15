from Clases.Persona import Persona
from Clases.Cuenta import Cuenta


def menu():
    print("--------------------------------------")
    print("Escoge una opción")
    print("1.- Depositar")
    print("2.- Retirar")
    print("3.- Mostrar resumen")
    print("4.- Solicitar un prestamo")
    print("5.- Apartado de Dedudas")
    print("6.- Salir")
    return input("\n")

n = input("Ingrese el nombre del titular de la cuenta: \n")
e = input("Ingrese la edad del titular: \n ")
persona1 = Persona(n,e)



r = ""

while r!= "4":

    r = menu()

    if r == "1":

        Cuenta.Depositar()


    elif r=="2":

        Cuenta.Retirar()


    elif r == "3":
        persona1.resumen()

    elif r == "4":
        Cuenta.SolicitarPres()

    elif r == "5":
        Cuenta.Deuda()



    elif r == "6":
        print("Hasta luego")


    else:
        print("No hay opción")



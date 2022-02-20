from Clases.Persona import Persona
from Clases.Operaciones import OP_Banco



def menu():
    print("--------------------------------------")
    print("Escoge una opción")
    print("1.- Depositar")
    print("2.- Retirar")
    print("3.- Abono")
    print("4.- Préstamo")
    print("5.- Mostrar resumen")
    print("S.- Salir")
    print("--------------------------------------")
    return input("\n")



n = input("Ingrese el nombre del titular de la cuenta: \n")
e = input("Ingrese la edad del titular: \n ")
persona1 = Persona(n,e)



r = ""

while r != "S":

    r = menu()

    if r == "1":
        persona1.cuenta.depositar()


    elif r=="2":

        persona1.cuenta.retirar()


    elif r== "3":
        OP_Banco.abono(persona1)


    elif r == "4":
        OP_Banco.prestamo(persona1)


    elif r == "5":
        persona1.resumen()


    elif r == "S":
        print("Hasta luego")


    else:
        print("No hay opción")


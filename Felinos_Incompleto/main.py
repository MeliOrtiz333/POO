from Clases.Felidae import *

mis_felinos = []

while r != "S":
    print("1.- Nuevo Felino")
    print("2.- Ver Felinos")
    print("3.- Actualizar animales")
    print("Pulse <S> para salir")
    r = input("Selecciona una opción: ")


    if r == "1":
        print("1.-Leopardo")
        print("2.-Puma")
        print("3.-Gato")
        g= input("Seleccione el felino")
        if g == "1": mis_felinos.append(Leopardo())
        elif g == "2": mis_felinos.append(Puma())
        elif g == "3": mis_felinos.append(Gato())
        else : print("Opción no válida")
import threading as th
import time

i = 0
j = 100
A = 0
print("\nBienvenido a alimentar al perro\n")


def Hambre():
    global i,j,A
    print("> ",i)
    i += 1
    A += 2
    hilo = th.Timer(5.0, Hambre)
    print("El hambre del perro es: ", A)
    hilo.start()

    if A == 10:

        NA = input("\n¿Desea alimentar al perro? (S/N)\n")
        time.sleep(3)
        if NA == "S":
            print("Se alimentó al perro\n")
            A = A - 5
            A += 2
            print("El hambre del perro es: ", A)

        elif NA == "N":
            print("¡Alimentalo!")

        else:
            print("No hay opción")


    if A >= 30:
        print("\nSe ha muerto el perro porque alcanzo 30 o más puntos de hambre :(\n")
        print("El programa ha terminado\n")
        hilo.cancel()


    if i > j:
        hilo.cancel()

Hambre()






import threading as th
from Perro import *

perro1 = perro("Firulais")



def crearHilo():
    global perro1
    hilo = th.Timer(2.0, crearHilo)
    perro1.darHambre()
    print(">>>>>>>>>>>>>>Hambre: ", perro1.hambre)

    if perro1.hambre > 10:

        r = input(perro1.Nombre+ "¡Tiene hambre!\n ¿Quieres alimentarlo? (Presione <S>)")
        if r == "S":
            perro1.alimentar(10)

    if perro1.hambre > 20:

        perro1.isAlive = False
        print("Horrible",perro1.Nombre, "ha muerto")
        hilo.cancel()
    else:

         hilo.start()

hilo = th.Timer(2.0,crearHilo)
hilo.start()



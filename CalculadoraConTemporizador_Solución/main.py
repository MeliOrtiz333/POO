import threading as th

a = 0
b = 0

def suma():
    a = int(input("Ingrese el primer número:  "))
    b = int(input("Ingrese el segundo número:  "))

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>Suma: ",(a + b))


def resta():
    a = int(input("Ingrese el primer número:  "))
    b = int(input("Ingrese el segundo número:  "))

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>Resta:   ",(a - b))


def multiplicacion():
    a = int(input("Ingrese el primer número:  "))
    b = int(input("Ingrese el segundo número:  "))

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>Multiplicación:  ", (a * b))


def division():
    a = int(input("Ingrese el primer número:  "))
    b = int(input("Ingrese el segundo número:  "))

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>División:  ", (a/b))


r = ' '
hilo = None

while r != 's':
    print("1.-Suma\n2.-Resta\n3.-Multiplicación\n4.-División\ns.-Salir")
    r = input()


    if r == '1':
        hilo = th.Timer(3.0,suma)
        hilo.start()
        hilo.join()


    elif r == '2':
        hilo = th.Timer(3.0, resta)
        hilo.start()
        hilo.join()


    elif r == '3':
        hilo = th.Timer(3.0, multiplicacion)
        hilo.start()
        hilo.join()


    elif r == '4':
         hilo = th.Timer(3.0, division)
         hilo.start()
         hilo.join()


    elif r == 's':

        print("Usted ha salido")
        hilo.cancel()

    else:
        print("No hay opción")
